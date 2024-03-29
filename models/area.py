from sqlalchemy import Column, types
from variables import conexion

class Area(conexion.Model):
  __tablename__ = 'areas'

  id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
  nombre = Column(type_=types.String(50), nullable=False, unique=True)
  piso = Column(type_=types.Integer, nullable=False, unique=True )