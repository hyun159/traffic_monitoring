# 2026_08_27

## git / docker 설치
## sudo생략, 비밀번호 생략
```
dnf install git -y


도커설치 메뉴얼
https://docs.docker.com/engine/install/centos

#관리 명령어 플러그인 설치
 sudo dnf -y install dnf-plugins-core

# 로컬 리포지토리에 docker 리포지토리URL 추가
 sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# 도커 패키지 설치
 sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin



# docker 명령어 sudo 비밀번호 생략
sudo visudo
nginx_01 ALL=(ALL) NOPASSWD: ALL

# docker 명령어 sudo 생략
sudo usermod -aG nginx_01 docker

```


## git에서 소스코드 가져오기
```
cd /opt
git clone URL
```

## nginx conf 파일 설정하기
## 바인드 볼륨으로 연결하기
## 버전관리 시 traffic.disable
```
mkdir -p /etc/nginx/conf.d
vi /etc/nginx/conf.d/traffic.conf
```


## nginx.conf 파일 기본구조
```


# 요청받을 http 요청은 server {} 으로 처리하기
server {

    # 포트(리스닝 소켓 개방)
    listen 80;
    
    # 도메인(host)
    server_name example.com;
    
    # url 경로(기능분기점)

    # 메인페이지
    location / {
        # 로컬에서 파일찾기
        root

        # 전달받을 서버
        proxy_pass http://10.0.2.20:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```


![컨테이너 포트 흐름](infra/images/nginx_port_flow.png)