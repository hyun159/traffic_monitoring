
from cctv import cctv
import os
import json
import redis
from dotenv import load_dotenv



# cctv 호출 함수
def service_cctv(cctv_id: int):
    return cctv.clients_cctv(cctv_id)





# redis 캐싱

load_dotenv()

# redis 연결 객체 생성
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    username=os.getenv("REDIS_USER"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True 
)



# redis에서 사용할 key(traffic)
TRAFFIC_CACHE_KEY = "traffic:data"


# 백엔드 scheduler -> service -> redis
# 5분 마다 레디스로 교통정보 갱신
def save_traffic(data):
    #set 명령어 실행
    redis_client.set(
        TRAFFIC_CACHE_KEY,
        json.dumps(data, ensure_ascii=False)
    )


# 자바스크립트 -> controller -> service -> redis
# redis에 저장된 최신 교통정보 조회
def get_traffic():

    #get 명령어 실행
    data = redis_client.get(TRAFFIC_CACHE_KEY)

    if data is None:
        return None

    return json.loads(data)



'''
# 전역 변수 캐싱
# 5분 API 갱신 함수


traffic_cache = None

# 백엔드(scheduler -> service) -> 캐시 (5분 주기)
# scheduler save_traffic에서 5분마다 API를 받음.
# global : 전역변수 호출 기능
def save_traffic(data):
    global traffic_cache
    traffic_cache = data

# 외부요청(5분 주기) <-> controller <-> service <-> 캐시 
# 자바스크립트가 5분 주기로 controller의 /traffic으로 데이터를 보낸다.
# service의 get_traffic은 캐시의 최신 값을 리턴한다. 
def get_traffic():
    return traffic_cache

'''