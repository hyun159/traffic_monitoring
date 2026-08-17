

# ITS API와 통신
# API_KEY .env 사용

import os
import httpx

API_URL = ""
API_KEY = os.getenv("API_KEY") #.env 인증키 호출


CCTV_NUM = {
        1: "창원CCTV 번호",
        2: "낙동강대교 CCTV 번호",
        3: "부산 고가도로 CCTV 번호"
    }


# CCTV 요청 함수
def clients_cctv(cctv_id):

    # 사용자요청 cctv 번호를 API의 실제 cctv 번호로 변환
    external_cctv_num = CCTV_NUM.get(cctv_id)

    # 요청 매개변수
    params = {
        "apikey":API_KEY,
        "CCTV번호" : external_cctv_num
        
    }

    # ITS API 요청
    response = httpx.get(
        API_URL,
        params=params,
        timeout=5.0,
    )

    # http 오류 확인
    response.raise_for_status()

    # HTTP 응답 변환
    data = response.json()

    return data[""]

# API 요청 함수
