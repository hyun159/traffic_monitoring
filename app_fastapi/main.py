

from fastapi import FastAPI
from controller import path
from fastapi.middleware.cors import CORSMiddleware
from scheduler.scheduler import scheduler


# 클래스 FastAPI로 객체 app 생성
app = FastAPI()

'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
'''



# 컨트롤러 데코레이트 path 호출
app.include_router(path.cctv_router)
app.include_router(path.traffic_router)
