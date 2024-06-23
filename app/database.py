from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# We write that by default of course with name/password and other
# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-adress/hostname>/<database>/'
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# we nned to create an engine that responsible for sqlalchemy to connect to postgress

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# creating the thing that is responsible for database connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# so basically it is copy pasting from documentation
Base = declarative_base()

# that is the function to connect to our database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
      
# that is for database connection  -> we can control and see what happening  
  
# while True: 
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Apasdauren2006', cursor_factory=RealDictCursor) # trying to connect (we do it in try because it can break). Host is our ip address.
#                                                                                                                 # cursor_factory it is for maintainance of the rows and coloums, that handles them.
#         cursor = conn.cursor() # executing sql statement

#         # if it is connected 
#         print("Database connected")
#         break

#     except Exception as error:
#         print("Connection failed")
#         print("Error:", error)
#         time.sleep(2)