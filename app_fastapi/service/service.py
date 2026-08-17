
from fastapi import FastAPI
import clients


# CCTV 요청 처리
def service_cctv(cctv_id: int):
    return clients.clients_cctv(cctv_id)