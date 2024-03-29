from flask import Flask
from flask_migrate import Migrate
from variables import conexion
from dotenv import load_dotenv
from os import environ
from models import *
from controllers import *
from flask_restful import Api

load_dotenv()

app = Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
conexion.init_app(app)

# Creo mis Migraciones
Migrate(app=app, db=conexion)

# Mis rutas
api.add_resource(AreaController, '/areas')
api.add_resource(AreaUnitarioController, '/area/<int:id>')
api.add_resource(EmpleadoController, '/empleados')

if __name__ == "__main__":
  app.run(debug=True)