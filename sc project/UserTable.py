import os
import sys
import datetime
from sqlalchemy import *
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine


 
Base = declarative_base()
 
 

class User(Base):
    __tablename__ = 'user_account'
   
    user_id = Column(Integer, primary_key = True, autoincrement=True)
    email_id = Column(String(30), unique=True)
    password=Column(String(20))

    def __init__(self,em,pw):
        self.email_id = em
        self.password= pw    

    def insertion(self):
        session.add(self)
        session.commit()

class Tenth(Base):
    __tablename__='tenth'
    id=Column(Integer,primary_key=True)
    title=Column(String)
    message=Column(String)
    timestamp=Column(DateTime,default=func.now())

    # def __repr__(self):
    #     return "<Blog(title='%s',message='%s',timestamp=)>" %(self.title,self.message)

    def __init__(self,title,message):
        self.title=title
        self.message=message
        #self.timestamp=datetime.datetime.now()

    def insertion(self):
        session.add(self)
        session.commit()

class Inter(Base):
    __tablename__='inter'
    id=Column(Integer,primary_key=True)
    title=Column(String)
    message=Column(String)
    timestamp=Column(DateTime,default=func.now())

    #def __repr__(self):
        #return "<Blog(title='%s',message='%s',timestamp=)>" %(self.title,self.message,self.timestamp)

    def __init__(self,title,message):
        self.title=title
        self.message=message
        #self.timestamp=datetime.datetime.now()

    def insertion(self):
        session.add(self)
        session.commit()

class Grad(Base):
    __tablename__='gradua'
    id=Column(Integer,primary_key=True)
    title=Column(String)
    message=Column(String)
    timestamp=Column(DateTime,default=func.now())

    #def __repr__(self):
        #return "<Blog(title='%s',message='%s',timestamp=)>" %(self.title,self.message,self.timestamp)

    def __init__(self,title,message):
        self.title=title
        self.message=message
        #self.timestamp=datetime.datetime.now()

    def insertion(self):
        session.add(self)
        session.commit()
 


engine = create_engine('sqlite:///UserAccounts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session=Session()
# book=session.query(Cart).filter_by(book_id=1).one()
# obj=Cart(1,1)
# obj.insertion()
