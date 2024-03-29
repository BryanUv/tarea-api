from flask_restful import Resource, request
from variables import conexion
from models import Empleado
from dtos import RegistrarEmpleadoDTO

class EmpleadoController(Resource):
  def get(self):
    empleado: list(Empleado) = conexion.session.query(Empleado).all()
    dto = RegistrarEmpleadoDTO()
    resultado = dto.dump(empleado, many=True)

    return {
      'content': resultado
    }
  
  def post(self):
    data = request.get_json()
    dto = RegistrarEmpleadoDTO()
    try:
      dataValidada = dto.load(data)

      nuevoEmpleado = Empleado(**dataValidada)
      conexion.session.add(nuevoEmpleado)
      conexion.session.commit()

      return {
        'message':'Empleado creado exitosamente'
      }
    
    except Exception as e:
      return {
        'message':'Error al crear la nuevo Empleado',
        'content':e.args
      },404