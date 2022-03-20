from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id      =   Column(Integer,primary_key=True,index=True)
    title   =   Column(String)
    rating  =   Column(Integer)
    created =   Column(DateTime(timezone=True),server_default=func.now())
    updated =   Column(DateTime(timezone=True),onupdate=func.now())
    
    authord_id  =   Column(Integer,ForeignKey('author.id',ondelete="CASCADE"))
    author      =   relationship("Author")

class Author(Base):
    __tablename__ = 'author'

    id      =   Column(Integer,primary_key=True,index=True)
    name    =   Column(String)
    age     =   Column(Integer)
    created =   Column(DateTime(timezone=True),server_default=func.now())
    updated =   Column(DateTime(timezone=True),onupdate=func.now())
