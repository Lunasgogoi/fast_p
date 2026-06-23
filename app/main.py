from typing import Optional,List
from fastapi import FastAPI, Response, status, HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal , get_db
from . import utils
from . routers import post, user , auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class posts(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="FastAPI",
            user="postgres",
            password="708635",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Hello World"}


