from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import ARRAY
from .database import Base

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, nullable=False)
    formula = Column(String, nullable=False)
    density = Column(Float, nullable=False)
    elements = Column(ARRAY(String), nullable=False)