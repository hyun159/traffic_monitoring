
from cctv import cctv



# cctv 호출 함수
def service_cctv(cctv_id: int):
    return cctv.clients_cctv(cctv_id)


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

