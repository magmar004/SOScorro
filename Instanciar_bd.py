from flask_sqlalchemy import SQLAlchemy

 #instanciamos la base de datos

db = SQLAlchemy()

#CREAMOS nuestro modelo de base datos
class Datos_usuario (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable = False) #nullable es que no puede ser nulo
    cedula_de_identidad = db.Column(db.String(7))
    tipo_de_sangre = db.Column(db.String(20))
    donante_de_organos = db.Column(db.String(20))
    alergia_a = db.Column(db.String(20))

    