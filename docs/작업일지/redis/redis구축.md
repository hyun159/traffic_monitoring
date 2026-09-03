
# 싱글 스레드
```
GET, SET, SADD 명령어 실행, 네트워크 처리 등 모든 작업은 메인 스레드가 동작함.
Redis 6.0 버전 부터 네트워크 패킷 읽기,쓰기는 I/O스레드가 멀티스레드로 동작.

실시간 쌓이는 GET, SET 패킷을 I/O 스레드가 병렬로 읽어와 메모리에 정렬.

메인 스레드가 GET, SET을 하나씩 처리함.
```

# 인메모리 영속성
```
레디스는 주로 데이터를 메모리에 저장

RDB -> 특정 시간마다 전체 스냅샷을 디스크 기록
AOF -> 모든 쓰기 명령을 로그로 기록 (파일커짐, 로딩 지연)
```

<hr/>
<hr/>
<hr/>


# OS 메모리 관리

## 메모리 오버커밋(Memory Overcommit)
### : 메모리 공간이 부족해 보이더라도 자식프로세스에게 가상공간 할당 요청을 허용한다.

```
시스템 콜 forck()는 부모프로세스와 자식프로세스를 동일한 물리 메모리 공간을 공유한다.

쓰기작업이 발생하면 해당 부분만 독립된 물리 메모리 공간이 할당된다.(COW - 쓰기 시 복사)
대체로 자식프로세스가 모든 페이지를 수정하지 않기 때문에 부모프로세스만큼의 물리공간이 필요하지 않다.

쓰기 작업이 몰리면 메모리 사용량이 순간 치솟을 수도 있기 때문에 메모리공간을 최소 30% ~ 50% 여유 있게 할당한다.
```

```bash
vm.overcommit_memort = 0

0 - 기본값 (약간 오버커밋허용)
1 - 항상 허용
2 - 오버커밋 제한
```

## THP(Transparent Huge Page)
### : 리눅스 커널이 메모리 페이지 크기를 자동으로 확장해서 관리하는 기능
```
기본 메모리 페이지는 4KB.
한 프로세스가 nGB 사용 시 몇 몇백개의 메모리 페이지 할당 해야함
CPU의 메모리 주소 변환 캐시(TLB)에 자원 증가

메모리 페이지를 2MB로 확장하면
TLB 자원이 줄어들고 주소변환 작업속도 향상

그런데 Redis를 사용 할 땐 THP 기능을 꺼야한다.
쓰기 작업이 잦으면 CoW 과정에서 변경될 데이터 마다 2MB로 단위로 묶여 있기에 순식간에 복사/정리 작업이 증가한다. CPU 지연과 병목현상 발생 가능성이 높다.
```

```bash
#GRUB 설정
sudo nano /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash transparent_hugepage=never"
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
sudo reboot
```
<hr/>
<hr/>
<hr/>

# Redis.conf 관리


## maxmemory
### : OOM Killer 방지
```

```

```bash
maxmemory 4gb
```


## maxmemory-policy
### : 메모리 초과 시 삭제 정책

```
volatile-lru : TTL 설정된 키 중 가장 사용하지 않는 데이터 삭제(권장)
allkeys-lru : 모든 키 중 가장 사용하지 않은 데이터 삭제
noeviction : 지우지 않고 쓰기 요청 시 에러를 반환한다(데이터 보존)
```

```bash
maxmemory-policy volatile-lru
maxmemory-policy allkeys-lru
maxmemory noeviction
```

## activedefrag
### : 데이터 삭제 후 메모리가 반환되지 않고 붕 뜨는 파편화 현상 자동 정리

```bash
activedefrag yes
```


<hr/>
<hr/>
<hr/>

# 메모리 관련 기본 명령어
```bash
free -h
swapon --show
vmstat 1  # si / so 값이 발생하면 swap 사용, 메모리 압박 가능성 높음

cat /proc/sys/vm/swappiness


```



# THP systemd 설정방법
```

리눅스2.6커널 이후  복잡한 계층 구조나 객체, 드라이버, 하드웨어 제어는 sysfs로 관리


sudo nano /etc/systemd/system/disable-thp.service

[Unit]
Description=Disable Transparent Huge Pages (THP) for Redis
After=sysinit.target local-fs.target

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'echo never > /sys/kernel/mm/transparent_hugepage/enabled && echo never > /sys/kernel/mm/transparent_hugepage/defrag'

[Install]
WantedBy=basic.target

# systemd 재로드
sudo systemctl daemon-reload

# 부팅 시 자동 실행 설정 및 즉시 시작
sudo systemctl enable --now disable-thp.service


cat /sys/kernel/mm/transparent_hugepage/enabled
cat /sys/kernel/mm/transparent_hugepage/defrag

```




<hr/>
<hr/>
<hr/>


# Redis 운영
[1번](#redis-데이터-영속성-관리)
```
RDB에 스냅샷파일, AOF에 명령어 로그 파일을 기록한다.

레디스 기본 설정상 RDB와 AOF의 저장 경로는 /data로 지정되어있음.
- dump.rdb
- appendonlydir/appendonly.aof
```

## 1.Redis 데이터 영속성 관리

바인드 마운트(사람), 네임드 마운트(컨테이너)의 차이는 관리 주체다.

1. conf 파일 생성
2. acl 파일 생성

/opt/redis/
├─ redis.conf
├─ users.acl
└─ docker-compose.yml


호스트에서 백업은 자체 관리
sudo mkdir -p /backup/redis
sudo chmod 750 /backup/redis


NFS 생성해서 붙이기


services:
  redis:
    image: redis:alpine
    container_name: redis
    command: redis-server --requirepass "your_password" --appendonly yes
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
      - ./redis.conf:/usr/local/etc/redis/redis.conf:ro # conf파일 바인드
      - ./users.acl:/usr/local/etc/redis/users.acl:ro # acl 파일 바인드
    restart: always
