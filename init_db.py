from flask import Flask
from Instanciar_bd import db, Datos_usuario

#Instanciamos de la clase flask usando el servidor 'app'
app = Flask('app')

#configuraciones de base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicializamos la base de datos
db.init_app(app)

#creamos la base de datos
with app.app_context():
    db.create_all()
