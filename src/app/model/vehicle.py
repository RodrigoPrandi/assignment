from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Vehicle(Base):
    id = Column(Integer, primary_key=True, index=True)
    distance = Column(Integer, index=True)
    owner = Column(String, index=True)