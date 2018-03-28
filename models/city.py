#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class City(BaseModel):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if environ.get('HBNH_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        name = Column(string(128), nullable=False)
        state_id = Column(string(60), ForeignKey("states.id"),
                          nullable=False)
    else:
        state_id = ""
        name = ""

# Reference: https://stackoverflow.com/questions/4906977/
# how-do-i-access-environment-variables-from-python
