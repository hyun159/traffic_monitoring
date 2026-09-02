
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
oo
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



swap
```