

from fastapi import FastAPI
import controller

# 클래스 FastAPI로 객체 app 생성
app = FastAPI

# 컨트롤러 데코레이트 path 호출
app.include_router(controller.path)
