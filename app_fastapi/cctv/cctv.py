

# ITS API와 통신
# API_KEY .env 사용

import os
import httpx
from dotenv import load_dotenv


load_dotenv()
API_URL = "https://openapi.its.go.kr:9443/cctvInfo"
API_KEY = os.getenv("API_KEY") #.env 인증키 호출

# 창원 요청변수
changwon = {
        "apiKey":API_KEY,
        "type":"its", # 도로유형 ( 고속도로 / its(국도) )
        "cctvType":"1",
        "minX":"128.72872896054545", # 최소 경도
        "maxX":"128.75991762189523", #최대 경도
        "minY": "35.18182667326473", #최소 위도
        "maxY": "35.18944966046303", #최대 위도
        "getType": "json"
        }


# 김해 요청변수
gimhae = {

}

# 부산 요청변수
busan = {

}



# CCTV 요청 함수
def clients_cctv(cctv_id):

    # 로컬변수와 API 요청변수 스위치 박스 생성
    cctv_params = {
        1: changwon,
        2: gimhae,
        3: busan
    }

   
    # 로컬변수와 API 요청변수 매핑
    selected_params = cctv_params[cctv_id]
        # ITS API 요청
    response = httpx.get(
        API_URL,
        params=selected_params,
        timeout=5.0
    )

    # http 오류 확인
    response.raise_for_status()

    # HTTP 응답 변환
    data = response.json()

    return data

# API 요청 함수
print(clients_cctv(1))