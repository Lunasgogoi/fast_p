from pydantic import BaseModel , ConfigDict , EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

#for users
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
    

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    model_config = ConfigDict(from_attributes=True)
    
    
class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    model_config = ConfigDict(from_attributes=True)




class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore
    
    

    