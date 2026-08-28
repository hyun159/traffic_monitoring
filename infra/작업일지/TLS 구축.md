
# 2026_08_28


## HTTPS 구축하기
```
[록키리눅스 Let's Encrypt SSL 키 생성 방법]
https://docs.rockylinux.org/zh/guides/security/generating_ssl_keys_lets_encrypt/?utm_source=chatgpt.com

# EPEL 저장소 활성화
sudo dnf config-manager --set-enabled crb

# 최신 EPEL 저장소 정보 설치
sudo dnf install epel-release -y

# /var/cache/dnf (캐시파일) 초기화, 새로고침
sudo dnf clean all
sudo dnf makecache

# 엔진엑스용 certbot 패키지 설치
dnf install certbot python3-certbot-nginx

# 엔진엑스 키 발급
sudo certbot certonly --standalone -d yulhatraffic.kro.kr

/etc/letsencrypt/live/yulhatraffic.kro.kr/fullchain.pem
/etc/letsencrypt/live/yulhatraffic.kro.kr/privkey.pem
```
