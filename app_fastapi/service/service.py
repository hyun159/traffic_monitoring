
from cctv import cctv
from scheduler import scheduler


# cctv 호출 함수
def service_cctv(cctv_id: int):
    return cctv.clients_cctv(cctv_id)


# 5분 API 갱신 함수 scheduler
# 

traffic_cache = None

# global : 전역변수에 값을 넣을 수 있음.
def save_traffic(data):
    global traffic_cache
    traffic_cache = data


def get_traffic():
    return traffic_cache