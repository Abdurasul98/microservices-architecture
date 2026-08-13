from fastapi import FastAPI
from app.urls import router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Post Service API", version="1.0.0")
app.include_router(router, prefix="/api")