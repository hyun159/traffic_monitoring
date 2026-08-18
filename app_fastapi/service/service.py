
from fastapi import FastAPI
import cctv


# CCTV 요청 처리
def service_cctv(cctv_id: int):
    return cctv.cctv(cctv_id)