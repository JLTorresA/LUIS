from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = "Personas"
    id = Column(Integer, primary_key=True,autoincrement=True)
    dni = Column(String)
    appPaterno = Column(String)
    appMaterno = Column(String)