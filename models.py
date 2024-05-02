from database import Base
from sqlalchemy import VARCHAR, String, Column, Integer

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    email=Column(VARCHAR(255),unique=True,index=True)
    password= Column(VARCHAR(255))