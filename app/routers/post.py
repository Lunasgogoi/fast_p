from fastapi import FastAPI, Response, status, HTTPException,Depends, APIRouter
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
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    
    
    posts = db.query(models.Post).all()
    
    return  posts

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PostResponse
)
def create_posts(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user),
):
    print(user_id)
    new_post = models.Post(**post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}",response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    return post

@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id:int , post: schemas.PostCreate, db: Session = Depends(get_db)):

    updated_post = db.query(models.Post).filter(models.Post.id == id)
    
    post_to_update = updated_post.first()
    
    if post_to_update == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )
    updated_post.update(post.dict(),synchronize_session=False) # type: ignore
    
    db.commit()
    
    return updated_post.first()

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )
    deleted_post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/test")
def test(current_user = Depends(oauth2.get_current_user)):
    return {"msg": "success"}