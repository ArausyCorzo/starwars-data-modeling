import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name= Column(String(8), nullable=False)
    first_name= Column(String(40), nullable=False)
    last_name= Column (String(40), nullable=False)
    email= Column(String(12), unique=True)
    




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')