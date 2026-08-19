
# 백그라운드에서 5분마다 실행
# controller <-> service(캐시쓰기 / DB쓰기) <-> scheduler <-> ITS API 요청
# 프론트엔드는 5분마다 controller 경로로 요청을 보낸다.

import os
import httpx
from dotenv import load_dotenv
from datetime import datetime, timedelta
from service import service

# 5분 마다 실행하는 라이브러리임
from apscheduler.schedulers.background import BackgroundScheduler


# API 요청변수 "fCastDate", "fCastHour" 사용에 필요함.
# 현재 시간 +5분, 당일 날짜 반영
now = datetime.now()
forecast_time = now + timedelta(minutes=5)
fCastDate = forecast_time.strftime("%Y%m%d")
fCastHour = forecast_time.strftime("%H")

# .env 호출
load_dotenv()


API_URL = "https://openapi.its.go.kr:9443/bypassFCastInfo"
API_KEY = os.getenv("API_KEY") #.env 인증키 호출





# 서부산종점 -> 가락IC
sectionId = ["39", "3901"]

def request_api():
    result = []

    for item in sectionId:

        
        response = httpx.get(
                API_URL,

                params = {
                "apiKey": API_KEY,
                "sectionId": item,
                "fCastDate": fCastDate,
                "fCastHour": fCastHour,
                "getType": "json"
                }
            )
       

    # HTTP 오류 확인
        response.raise_for_status()
    
    # HTTP 응답 변환
        data = response.json()

   # 결과값 추가
        result.append(data)
    

    return result

print(request_api())

# result 값을 service로 전달하는 함수
# 5분마다 실행해야하므로 
def update_traffic():
    data = request_api()
    service.save_traffic(data)


scheduler = BackgroundScheduler()

scheduler.add_job(
    request_api,
    "interval",
    minutes=5
)

scheduler.start()