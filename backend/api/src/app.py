from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.v1.api import router

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.include_router(router, prefix="/api/v1")
