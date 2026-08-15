
from fastapi import FastAPI

# 공공 api CCTV URL 목록
cctv_path = {
    1: "",
    2: "",
    3: ""
}

# controller의 함수 def get_cctv(cctv_id: int) 호출
# 매개변수 cctv_id의 값은 1~3
# service_cctv는 1~3의 숫자를 받고
# 공공 api url을 리턴한다.

def service_cctv(cctv_id: int):
    url = cctv_path[cctv_id]
    return url