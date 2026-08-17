

# Controller
# 외부 사용자의 HTTP 요청에 대한 응답
# CCTV 영상 요청

# 코드 흐름 : CCTV 요청 -> Controller -> Service -> Clients -> ITS API


# 모듈화 클래스 APIRouter 호출
from fastapi import APIRouter

# service 파일 호출
from service.service import service

#객체 생성
router = APIRouter(
    prefix="/cctv", # CCTV URL
    tags=["CCTV"], 
    responses={404: {"description": "Not Found"}}
)

# 정적웹으로 부터 cctv 번호 요청 받는다.
# service로 cctv_id(cctv 번호) 전달
# service에게 받은 공공 api cctv url 반환
@router.get("/{cctv_id}") # 요청 받는 번호
def get_cctv(cctv_id: int): # 매개변수 번호와 service 함수 호출
    return service.service_cctv(cctv_id)
