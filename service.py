#------------------------------IMPORT------------------------------#
from flask import Flask, render_template, request, redirect, url_for, abort

#-------------------------------INIT-------------------------------#
#-------------FLASK-------------#
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webservice.db/'
app.config['SECRET_KEY'] = "random string"

#----------SQL-ALCHEMY----------#
db = SQLAlchemy(app)

#-----------------------------MODELOS------------------------------#
#------------USUARIO------------#
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    password = db.Column(db.String(100))

def __init__(self, user, password):
   self.user = user
   self.password = password

#------------MENSAJE------------#
class Mensaje(db.Model):
    __tablename__ = 'mensajes'
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.String(100))
   
def __init__(self, chat):
   self.contenido = contenido

#-------------ENVIO-------------#
class Envio(db.Model):
    __tablename__ = 'envios'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    mensaje_id = db.Column(db.Integer, db.ForeignKey('mensajes.id'))
   
def __init__(self, usuario_id, mensaje_id):
   self.usuario_id = usuario_id
   self.mensaje_id = mensaje_id

#----------------------------FUNCIONES---------------------------#

def validate_login(form):
	success = False

	return success

#------------------------------RUTAS-----------------------------#
#------------DEFAULT-----------#
@app.route('/')
def index():
    return render_template('index.html')

#-------------LOGIN------------#
@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		if validate_login(request.form):
			return redirect(url_for('chat'))
		else:
			abort(400)
	else: 
		return render_template('login.html')

#-------------CHAT-------------#
@app.route('/chat')
def chat():
    return render_template('chat.html')

#--------------------------ERROR-HANDLER-------------------------#
#---------RUTA-INVALIDA--------#
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

#--------LOGIN-INVALIDO--------#
@app.errorhandler(400)
def invalid_login(error):
    return redirect(url_for('login'))

#------------------------------MAIN------------------------------#
if __name__ == '__main__':
	db.create_all()
    app.run(host='0.0.0.0')