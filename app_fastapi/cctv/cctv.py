

# cctv 파일
# 사용자 cctv 영상 요청 <-> controller <-> service <-> cctv <-> ITS 영상 요청



import os
import httpx
from dotenv import load_dotenv

# .env 호출
load_dotenv()

API_URL = "https://openapi.its.go.kr:9443/cctvInfo"
API_KEY = os.getenv("API_KEY") #.env 인증키 호출


장유IC = {
        "apiKey":API_KEY,
        "type":"ex", # 도로유형 ( 고속도로 / its(국도) )
        "cctvType":"1",
        "minX":"128.80815571121036", # 최소 경도
        "maxX":"128.80870127206373", #최대 경도
        "minY":"35.19691939528175", #최소 위도
        "maxY":"35.19731956808292", #최대 위도
        "getType":"json"
        }



#(남해2지선[장유])
김해응달교 = {
        "apiKey":API_KEY,
        "type":"its", # 도로유형 ( 고속도로 / its(국도) )
        "cctvType":"1",
        "minX":"128.83039287446073", # 최소 경도
        "maxX":"128.83122063648221", #최대 경도
        "minY":"35.176863845419014", #최소 위도
        "maxY":"35.178045421219906", #최대 위도
        "getType":"json"
        }


# 사상 나들목 ,종점
사상나들목 = {
        "apiKey":API_KEY,
        "type":"ex", # 도로유형 ( ex(고속도로) / its(국도) )
        "cctvType":"1",
        "minX":"128.96268666935387", # 최소 경도
        "maxX":"128.97401248679498", #최대 경도
        "minY":"35.15209623524839", #최소 위도
        "maxY":"35.15383032786352", #최대 위도
        "getType":"json"

}




# CCTV 요청 함수
def clients_cctv(cctv_id):

    # 로컬변수와 API 요청변수 스위치 박스 생성
    cctv_params = {
        1: 장유IC,
        2: 김해응달교,
        3: 사상나들목
    }

   
    # 로컬변수와 API 요청변수 매핑
    # 장유IC = cctv_params[1]
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
