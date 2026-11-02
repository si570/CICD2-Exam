from fastapi import Depends, FastAPI, HTTPException,status
from fastapi.responses import Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Select
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base, UserDB
from app.schemas import UserRead

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

@app post("/api/user", Response_model=UserRead,status_code=status.HTTP_201_CREATED)

def loans(new_user:create,db:Session = Depends(get_db)):
db_user=UserDB(id=new_User.User_id, *new_user.model_dump
               (exclude={"user_id"})
               )
  db.add(db_user) 
try:
   db.commit()
  db.refresh(db_user) 
except IntegrityError:
db.rollback()
raise HTTPException(Status_code=status.HTTP_409_CONFLICT)
detail = ("A user with this email exists")

return db_user

@app.get("/api/users",response_model=UserRead)
def getUsers( 
   db:Session=Depends(get_db)):
   statment=Select(userDB).Order_by(UserDB).order_by(UserDB.id)
   return db.excute(statment).scatars().all()


@app.get("api/users",response_model = list[UserRead])
def get_user(User_id:int,db: Session= Depends (get_db)):
  db_user= db.get(UserDB,user_id)
  if db_user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail ="User Not found")
  )

  return db_user

app.delete("/api/users",response_model=UserRead)
  def get_user(User_id:int,db: Session= Depends (get_db)):
  db_user= db.get(UserDB,user_id)
  if db_user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail ="User Not found")
  )



