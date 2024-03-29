from marshmallow import Schema, fields

class RegistrarEmpleadoDTO(Schema):
  nombre = fields.String(required=True, error_messages={
    'required':'El nombre es obligatorio'
  })
  apellido = fields.String(required=True, error_messages={
    'required':'El apellido es obligatorio'
  })
  email = fields.String(required=True, error_messages={
    'required':'El email es obligatorio'
  })