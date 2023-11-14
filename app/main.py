from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import personas
from db import  engine
from models.persona import Base

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(personas.router, prefix="/api")

