from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Schema -> is the way we define the structure of request & response
class PostBase(BaseModel): # extend basemodel
    title: str
    content: str    
    published: bool = True # by default it is True, it will appear if there will no responce

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
# for each Session: get/post and other, we can specify which data should we send as a response to user
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
        
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
    dir: int = Field(..., le=1)
    