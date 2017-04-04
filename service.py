#------------------------------IMPORT------------------------------#
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
#------------------------------------------------------------------#




#-------------------------------INIT-------------------------------#
#-------------FLASK-------------#
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webservice.db/'
app.config['SECRET_KEY'] = "random string"
#-------------------------------#


#----------SQL-ALCHEMY----------#
db = SQLAlchemy(app)
#-------------------------------#
#------------------------------------------------------------------#




#-----------------------------MODELOS------------------------------#
#------------USUARIO------------#
class Usuario(db.Model):
	__tablename__ = 'usuarios'
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))

	def __init__(self, user, password):
		self.user = user
		self.password = password
#-------------------------------#


#------------MENSAJE------------#
class Mensaje(db.Model):
	__tablename__ = 'mensajes'
	id = db.Column(db.Integer, primary_key=True)
	contenido = db.Column(db.String(100))
   
	def __init__(self, contenido):
		self.contenido = contenido
#-------------------------------#


#-------------ENVIO-------------#
class Envio(db.Model):
	__tablename__ = 'envios'
	id = db.Column(db.Integer, primary_key=True)
	usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	mensaje_id = db.Column(db.Integer, db.ForeignKey('mensajes.id'))
   
	def __init__(self, usuario_id, mensaje_id):
		self.usuario_id = usuario_id
		self.mensaje_id = mensaje_id
#-------------------------------#
#----------------------------------------------------------------#




#----------------------------FUNCIONES---------------------------#
#-------------LOGIN-------------#
def validate_login(form):
	success = False
	usuario = Usuario.query.filter_by(user=form['user']).first();
	if usuario:
		if usuario.password == form['password']:
			success = True
	return success
#-------------------------------#


#------------REGISTER-----------#
def do_register(form):
	usuario = Usuario(form['user'], form['password'])
	db.session.add(usuario)
	db.session.commit()
	return
#-------------------------------#
#----------------------------------------------------------------#




#------------------------------RUTAS-----------------------------#
#------------DEFAULT------------#
@app.route('/')
def index():
    return render_template('index.html')
#-------------------------------#


#-------------LOGIN-------------#
@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		if validate_login(request.form):
			return redirect(url_for('chat'))
		else:
			abort(400)
	else: 
		return render_template('login.html')
#-------------------------------#


#------------REGISTER-----------#
@app.route('/register', methods=['POST', 'GET'])
def register():
	if request.method == 'POST':
		do_register(request.form)
		return redirect(url_for('usuarios'))
	else: 
		return render_template('register.html')
#-------------------------------#


#--------LISTA-USUARIOS---------#
@app.route('/usuarios')
def usuarios():
    return render_template('show_all.html', usuarios = Usuario.query.all() )
#-------------------------------#


#-------------CHAT--------------#
@app.route('/chat')
def chat():
	
    return render_template('chat.html')
#-------------------------------#
#----------------------------------------------------------------#





#--------------------------ERROR-HANDLER-------------------------#
#---------RUTA-INVALIDA---------#
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
#-------------------------------#


#--------LOGIN-INVALIDO---------#
@app.errorhandler(400)
def invalid_login(error):
    return redirect(url_for('login'))
#-------------------------------#
#----------------------------------------------------------------#




#------------------------------MAIN------------------------------#
if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)
#----------------------------------------------------------------#
