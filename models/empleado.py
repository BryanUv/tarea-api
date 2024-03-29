from sqlalchemy import Column, types, ForeignKey
from variables import conexion

class Empleado(conexion.Model):
  __tablename__ = 'empleados'

  id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
  nombre = Column(type_=types.String(30), nullable=False)
  apellido = Column(type_=types.String(40), nullable=False)
  email = Column(type_=types.String(100), unique=True, nullable=False)

  area = Column(ForeignKey(column='areas.id'), name='area_id', nullable=False)