from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Stock Intelligence API")

app.include_router(router)