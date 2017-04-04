from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webservice.db/'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    password = db.Column(db.String(100))

def __init__(self, user, password):
   self.user = user
   self.password = password

class Mensaje(db.Model):
    __tablename__ = 'mensajes'
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.String(100))
   
def __init__(self, chat):
   self.contenido = contenido

class Envio(db.Model):
    __tablename__ = 'envios'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    mensaje_id = db.Column(db.Integer, db.ForeignKey('mensajes.id'))
   
def __init__(self, usuario_id, mensaje_id):
   self.usuario_id = usuario_id
   self.mensaje_id = mensaje_id

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)