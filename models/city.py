#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """ The class City representation of MySql Database. 

    Inherits from SQLAlchemy Base and links to the MySql table cities.

    Attributes:
    __tablename__(str): Table name to store cities. 
    name(str): The name of the city.
    state_id(str): The state id of the city. 
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
