from flask_restful import Resource, request
from variables import conexion
from models import Area
from dtos import RegistrarAreaDTO

class AreaController(Resource):
  def get(self):
    areas: list(Area) = conexion.session.query(Area).all()
    dto = RegistrarAreaDTO()
    resultado = dto.dump(areas, many=True)

    return {
      'content': resultado
    }
  
  def post(self):
    data = request.get_json()
    dto = RegistrarAreaDTO()
    try:
      dataValidada = dto.load(data)

      nuevaArea = Area(**dataValidada)
      conexion.session.add(nuevaArea)
      conexion.session.commit()

      return {
        'message':'Area creada exitosamente'
      }
    
    except Exception as e:
      return {
        'message':'Error al crear la nueva Area',
        'content':e.args
      },404

class AreaUnitarioController(Resource):
  dto = RegistrarAreaDTO()
  def get(self, id):
    try:
      area = conexion.session.query(Area).filter_by(id=id).first()
      resultado = self.dto.dump(area)
      if not area:
        raise Exception('El area no se encontro')
      
      return {
        'content': resultado
      }
    except Exception as e:
      return {
        'message':'No se encontro el area'
      },404