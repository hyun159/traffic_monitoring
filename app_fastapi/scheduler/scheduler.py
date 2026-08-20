
# 백그라운드에서 5분마다 실행
# (받는쪽)controller <-> service(캐시쓰기 / DB쓰기) <-> (보내는쪽)scheduler <-> ITS API 요청
# cctv는 사용자 호출 때 데이터를 보냄
# scheduler는 5분 마다 service로 데이터를 보냄

import os
import httpx
from dotenv import load_dotenv
from datetime import datetime, timedelta
from service import service

# 5분 마다 실행하는 라이브러리임
from apscheduler.schedulers.background import BackgroundScheduler


# API 요청변수 "fCastDate", "fCastHour" 사용에 필요함.

now = datetime.now() # 현재 날짜 + 현재 시간

# 분 단위가 30분 이상이면 반올림, API 시간요청값이 시(H) 단위로만 요청가능함.
# 예를들어 현재시간 12시 45분이라면 반올림하여 13시로 변수값 할당
# 12시 27분이라면 12시로 변수값 할당
if now.minute >= 30:
    rounded_time = (now + timedelta(hours=1)).replace(minute=0, second=0)
else:
    rounded_time = now.replace(minute=0, second=0, microsecond=0)

fCastHour = rounded_time.strftime("%H")
fCastDate = rounded_time.strftime("%Y%m%d")

# .env 호출
load_dotenv()


API_URL = "https://openapi.its.go.kr:9443/bypassFCastInfo"
API_KEY = os.getenv("API_KEY") #.env 인증키 호출




# sectionId는 한국도로공사에서 지정한 도로 번호.
# 39 : 서부산에서 가락ic
# 3901 : 가락ic에서 서부산
sectionId = ["39", "3901"]



# linkId : 도로를 나타내는 번호
target_linkId = {
    
        "1411062000": {
            "도로": "낙동대교",
            "방향": "부산",
            "위치": "낙동대교 시작"
        },

       
        "1440068100":{
            "도로": "낙동대교",
            "방향": "부산",
            "위치": "낙동대교 종점"
        },


        "1440068000": {
            "도로": "낙동대교",
            "방향": "김해",
            "위치": "낙동대교 시작"
        },

        "1411061900": {
            "도로": "낙동대교",
            "방향": "김해",
            "위치": "낙동대교 종점"
        }
    }



# ITS는 sectionId 갯수만큼 API의 헤더를 응답한다.
# JSON의 헤더 갯수 = 도로섹션 값이므로 섹션 갯수 만큼 for문으로 나눈다.
# 1개 헤더는 sectionId 갯수만큼 데이터가 존재한다.
# 따라서 for문을 사용하여 헤더를 1개씩 돌리고
# 이중 for문으로 헤더 내부 linkId 갯수만큼 돌린다.

# 원본 데이터 형식
'''
헤더[body[items]]
헤더[body[items]]

    {
    "header": {...},
    "body": {
        "totalCount": 75,
        "items": [
            {...},
            {...},
            ...
        ]
    }
}
''' 


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


    # body의 값만큼 반복
    # 1개 데이터 형태
    # {'fcastDate': '20260820', 'fcastHour': '14', 'linkId': '1410002400', 'sectionId': '39', 'sectionType': 'D', 'detourId': '39', 'length': '95.8', 'speed': '62.7'}
    
    userData = []
    # 응답받은 도로 헤더갯수 만큼 반복
    for response_data in result:
        # 도로 헤더 내부 items 값 만큼 반복
        for item in response_data["body"]["items"]:

        #target_linkid안에서 linkId와 동일한 번호를 찾는다.
            if item["sectionType"] == "M" and item["linkId"] in target_linkId:
               parsed_data = {
                   "날짜": item["fcastDate"],
                   "시간": item["fcastHour"],
                   "도로": target_linkId[item["linkId"]]["도로"],
                   "방향": target_linkId[item["linkId"]]["방향"],
                   "위치": target_linkId[item["linkId"]]["위치"],
                   "평균 속력": item["speed"]

               }
               userData.append(parsed_data)





    return userData

print(request_api())

'''
# result 값을 service로 전달하는 함수
# 5분마다 실행해야하므로 
def update_traffic():
    data = request_api()
    service.save_traffic(data)


# 5분 주기 스케쥴링
scheduler = BackgroundScheduler()

scheduler.add_job(
    request_api,
    "interval",
    minutes=5
)

scheduler.start()
'''