from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):
  __tablename__ = "product"

  id = Column(Integer, primary_key=True)
  name = Column(String)
  price = Column(Float)