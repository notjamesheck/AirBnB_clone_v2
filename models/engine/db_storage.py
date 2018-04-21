#!/usr/bin/python3

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
import models
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class_list = [City, State, User, Place, Review, Amenity]

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}


class DBStorage:
    """ Defines database storage """

    __engine = None
    __sesion = None

    def __init__(self):
        """ Init a DBStorage object """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                environ.get("HBNB_MYSQL_USER"),
                environ.get("HBNB_MYSQL_PWD"),
                environ.get("HBNB_MYSQL_HOST"),
                environ.get("HBNB_MYSQL_DB")), pool_pre_ping=True)

        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries all objects in current DB session against cls """
        results = {}

        for key, val in classes.items():
            if cls == key:
                for value in self.__session.query(classes[key]):
                    key = "{}.{}".format(value().__class__.__name__, value.id)
                    results[key] = value
            else:
                for a_class in class_list:
                    for value in self.__session.query(a_class):
                        key = "{}.{}".format(value().__class__.__name__,
                                             value.id)
                        results[key] = value

            return (results)

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped = scoped_session(Session)
        self.__session = scoped()

    def close(self):
        """ Heres a comment """
        self.__session.close()
