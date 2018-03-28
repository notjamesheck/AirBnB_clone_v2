#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import environ


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if environ.get("HBNB_TYPE_STORAGE") != "db":
        email = ""
        password = ""
        first_name = ""
        last_name = ""
