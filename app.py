from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios/'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

def __init__(self, first_name, last_name):
   self.first_name = first_name
   self.last_name = last_name

class mensaje(db.Model):
    __tablename__ = 'mensajes'
    id = db.Column(db.Integer, primary_key=True)
    chat = db.Column(db.String(100))
   
def __init__(self, chat):
   self.chat = chat

class envio(db.Model):
    __tablename__ = 'envios'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(100))
    mensaje_id = db.Column(db.String(100))
   
def __init__(self, usuario_id, mensaje_id):
   self.usuario_id = usuario_id
   self.mensaje_id = mensaje_id

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)