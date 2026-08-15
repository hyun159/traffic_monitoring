
# 모듈화 클래스 APIRouter 호출
from fastapi import APIRouter

# service 파일 호출
from service import service

#객체 생성
router = APIRouter(
    prefix="/cctv",
    tags=["CCTV"],
    responses={404: {"description": "Not Found"}}
)

# 정적웹으로 부터 cctv 번호 요청 받는다.
# service로 cctv_id(cctv 번호) 전달
# service에게 받은 공공 api cctv url 반환
@router.get("/{cctv_id}")
def get_cctv(cctv_id: int):
    return service.service_cctv(cctv_id)
