#!/usr/bin/python3
'''
    Implementation of the State class
'''
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")

        '''
        @property
        def cities(self):
            matching_cities = []
            for city in self.cities:
                if city.state_id == self.id:
                    matching_cities.append(city)

            return (matching_cities)
        '''
    else:
        '''
        name = ""
        '''
        @property
        def cities(self):
            matching_cities = []
            cities = models.storage.all(City)
            for city, info in cities.items():
                if info.state_id == self.id:
                    matching_cities.append(city)

            return matching_cities

# Ref: https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete
