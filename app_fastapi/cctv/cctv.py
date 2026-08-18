

# cctv 파일
# 사용자 cctv 영상 요청 <-> controller <-> service <-> cctv <-> ITS 영상 요청



import os
import httpx
from dotenv import load_dotenv

# .env 호출
load_dotenv()

API_URL = "https://openapi.its.go.kr:9443/cctvInfo"
API_KEY = os.getenv("API_KEY") #.env 인증키 호출

# 창원 요청변수
창원 = {
        "apiKey":API_KEY,
        "type":"its", # 도로유형 ( 고속도로 / its(국도) )
        "cctvType":"1",
        "minX":"128.780000", # 최소 경도
        "maxX":"128.850000", #최대 경도
        "minY": "35.150000", #최소 위도
        "maxY": "35.210000", #최대 위도
        "getType": "json"
        }



김해응달교 = {
        "apiKey":API_KEY,
        "type":"its", # 도로유형 ( 고속도로 / its(국도) )
        "cctvType":"1",
        "minX":"128.83019242491838", # 최소 경도
        "maxX":"128.83098043278983", #최대 경도
        "minY": "35.17649062377582", #최소 위도
        "maxY": "35.17785754845648", #최대 위도
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
        1: 창원,
        2: gimhae,
        3: busan,
        4: 김해응달교
    }

   
    # 로컬변수와 API 요청변수 매핑
    selected_params = cctv_params[cctv_id]
        # ITS API 요청
    response = httpx.get(
        API_URL,
        params=selected_params,
    )

    # http 오류 확인
    response.raise_for_status()

    # HTTP 응답 변환
    cctv_data = response.json()


    cctv_data = {
    "cctvname": cctv_data["response"]["data"]["cctvname"],
    "cctvurl": cctv_data["response"]["data"]["cctvurl"]

}
    return cctv_data

if __name__ == "__main__":
    print(clients_cctv(4))