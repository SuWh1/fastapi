from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# that codes creates the tables in database
# models.Base.metadata.create_all(bind=engine)
# it looks for a tablename in models.py, and if finds it it will do nothing (not refresh it)
# and for tha3t we can use another libraris, for example: ALEMBIC

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
            
app.include_router(post.router)
app.include_router(user.router) 
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello to madi"}
    
    
# я красивая принцесса