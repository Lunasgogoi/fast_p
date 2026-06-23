from fastapi import FastAPI, Response, status,APIRouter, HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from .. import models, schemas
from .. database import engine, SessionLocal , get_db
from .. import utils
from typing import List
from .. import oauth2

router = APIRouter(
    prefix="/users",
    
    tags=["Users"]
)

# FOR THE USER MODEL

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    
    print(user.password)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}',response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} does not exist",
        )
        
    return user


