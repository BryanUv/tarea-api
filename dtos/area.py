from marshmallow import Schema, fields

class RegistrarAreaDTO(Schema):
  nombre = fields.String(required=True, error_messages={
    'required':'El nombre es obligatorio'
  })
  piso = fields.Integer(required=True, error_messages={
    'required':'El piso es obligatorio'
  })