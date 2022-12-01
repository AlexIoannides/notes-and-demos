"""
All data Models can be found here.
"""
from typing import Any, Dict

from sqlalchemy import (
    Column,
    Float,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Person(Base):
    """Personal information."""
    
    __tablename__ = "person"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    address_id = Column(Integer, ForeignKey("address.id"))
    name = Column(String, nullable=False)
    age = Column(Float, nullable=False)
    
    address = relationship("Address", back_populates="person")

    def dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "address": self.address_id,
            "name": self.name,
            "age": self.age
        }


class Address(Base):
    """Address information."""
    
    __tablename__ = "address"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postcode = Column(String, nullable=False)

    person = relationship("Person", back_populates="address")
    
    def dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "street": self.street,
            "city": self.city,
            "postcode": self.postcode
        }

