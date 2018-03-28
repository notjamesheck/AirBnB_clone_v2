#!/usr/bin/python3
'''
    Implementation of the State class
'''

import models
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel):
    '''
        Implementation for the State.
    '''

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        print("database all over the place")
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        cities = relationship("City", cascade="all, delete-orphan",
                              backref="State")
    else:
        name = ""

        @property
        def cities(self):
            collection = models.storage.all("City").value()
            matching_cities = []

            for record in collection:
                if record.id == self.id:
                    matching_cities.append(record)

            return (matching_cities)


#Ref: https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete
