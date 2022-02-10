import datetime as _dt
import email
from sqlalchemy import Column,String,Integer,DateTime
from db import db_connection as _db

class Contact(_db.Base):
    __tablename__ = "contacts"

    id          =   Column(Integer,primary_key=True,index=True)
    first_name  =   Column(String,index=True)
    last_name   =   Column(String,index=True)
    email       =   Column(String,index=True,unique=True)
    phone_number    =   Column(String,index=True,unique=True)
    created_at  =   Column(DateTime,default=_dt.datetime.utcnow)
