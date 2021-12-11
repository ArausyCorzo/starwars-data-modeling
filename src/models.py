import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name= Column(String(8), nullable=False)
    first_name= Column(String(40), nullable=False)
    last_name= Column (String(40), nullable=False)
    email= Column(String(12), unique=True)
    favorites= relationship("Favorites", back_populates="parent")

class Favorites(Base):
    __tablename__ = 'favorites'
    id= Column(Integer, primary_key=True)
    element_name= Column(String(20), nullable=False)
    amount= Column(Integer, default=0)
    users_id= Column(Integer, ForeignKey("users.id"))
    users= relationship("Users", back_populates="children")
    # planets= relationship("Planets")
    # characters= relationship("Characters")

class Planets(Base):
    __tablename__= 'planets'
    id= Column(Integer, primary_key=True)
    name= Column(String(20), nullable=False)
    population= Column(Float)
    terrain= Column(String, nullable=False)
    favorites_id= Column(Integer, ForeignKey("favorites.id"))

class Characters(Base):
    __tablename__= 'characters'
    id= Column(Integer, primary_key=True)
    name= Column(String(10), nullable=False)
    hair_color= Column(String(8), nullable=False)
    eyes_color= Column(String(8), nullable=False)
    description= Column(String(200), nullable=False)
    favorites_id= Column(Integer, ForeignKey("favorites.id"))

class Vehicles(Base):
    __tablename__= 'Vehicles'
    id= Column(Integer, primary_key=True)
    name= Column(String(10), nullable=False)
    name_pilot= Column(String(40), nullable=False)
    passenger= Column(Integer)
    favorites_id= Column(Integer, ForeignKey("favorites.id"))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')