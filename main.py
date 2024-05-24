from fastapi import FastAPI, HTTPException, Query, Depends
from database import Base, SessionLocal, engine
from models import User
from pydantic import BaseModel, PydanticUserError
from typing import Optional, List
from sqlalchemy.orm import Session
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserSchema(BaseModel):
    name: str
    email: str
    class Config:
        arbitrary_types_allowed=True

class UserCreateSchema(UserSchema):
    password: str

@app.get("/users", response_model=List[UserSchema])
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()

@app.post("/users",response_model=UserSchema)
def create_user(user: UserCreateSchema, db:Session=Depends(get_db)):
    u=User(name=user.name, email=user.email,password=user.password)
    db.add(u)
    db.commit()
    return u

@app.put("/users/{user_id}",response_model=UserSchema)
def update_user(user_id: int, user: UserSchema, db:Session=Depends(get_db)):
    try:
        u=db.query(User).filter(User.id==user_id).first()
        u.name=user.name
        u.email= user.email
        db.add(u)
        db.commit()
        return u
    except:
        return HTTPException(status_code=404, detail = "user not found")
    
@app.delete("/users/{user_id}", response_class=JSONResponse)
def delete_user(user_id: int, db:Session=Depends(get_db)):
    try:
        u=db.query(User).filter(User.id==user_id).first()
        db.delete(u)
        db.commit()
        return{f"User of id {user_id} has been deleted":True}
    except:
        return HTTPException(status_code=404, detail = "user not found")
