
from cctv import cctv



# cctv 호출 함수
def service_cctv(cctv_id: int):
    return cctv.clients_cctv(cctv_id)


# 5분 API 갱신 함수 scheduler
# 

traffic_cache = None

# scheduler 함수에서 data값을 받음.
# global : 전역변수에 값을 넣을 수 있음.
def save_traffic(data):
    global traffic_cache
    traffic_cache = data

# controller로 값을 보냄
def get_traffic():
    return traffic_cache