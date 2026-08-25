

# Controller
# 외부 사용자의 HTTP 요청에 대한 응답
# CCTV 영상 요청

# 코드 흐름 : CCTV 요청 -> Controller -> Service -> Clients -> ITS API


# 모듈화 클래스 APIRouter 호출
from fastapi import APIRouter

# service 파일 호출
from service import service

# scheduler 파일 호출
from scheduler import scheduler

#객체 생성
cctv_router = APIRouter(
    prefix="/cctv", # CCTV URL
    tags=["CCTV"], 
    responses={404: {"description": "Not Found"}}
)


# CCTV 버튼 기능
# 정적웹으로 부터 cctv 번호 요청 받는다.
# service로 cctv_id(cctv 번호) 전달
# service에게 받은 공공 api cctv url 반환
@cctv_router.get("/{cctv_id}") # 요청 받는 번호
def get_cctv(cctv_id: int): # 매개변수 번호와 service 함수 호출
    return service.service_cctv(cctv_id)



#객체 생성
traffic_router = APIRouter(
    prefix="/traffic", # traffic URL
    tags=["traffic"], 
    responses={404: {"description": "Not Found"}}
)



# 5분 주기 교통 정보 갱신 기능
# (백그라운드)
# shceduler가 5분마다 service로 데이터 전달
# service의 전역함수에 데이터 5분 주기 갱신
# (사용자 요청 시)
# 자바스크립트 5분 주기 요청 -> controller
# service -> controller -> 자바스크립트 
@traffic_router.get("")
def get_5min_info():
    return service.get_traffic()