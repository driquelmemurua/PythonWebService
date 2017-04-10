#------------------------------IMPORT------------------------------#
from flask import Flask, render_template, request, url_for, redirect, session
import requests
import queue
import json
from requests.exceptions import ConnectionError

#------------------------------------------------------------------#




#-------------------------------INIT-------------------------------#
#-------------FLASK-------------#
app = Flask(__name__)
app.secret_key = 'Kira did nothing wrong'
#-------------------------------#

#-------------MAP-------------#
mapaCola = {}
#-----------------------------#


#------------------------------------------------------------------#


#------------------------------RUTAS-----------------------------#
#------------DEFAULT------------#
@app.route('/')
def index():
	return render_template('index.html')
#-------------------------------#


#------------MENSAJE------------#
@app.route('/mensajes', methods=['POST', 'GET'])
def mensajes():

	headers = {"Authorization":session['token']}
	if request.method == 'POST':
		try:
			payload = {'contenido':request.form['contenido']}
			url = 'http://localhost:5001/mensajes'
			if not (session['token'] in mapaCola):
				mapaCola[session['token']] = queue.Queue()
			mapaCola[session['token']].put(payload)	
			while not mapaCola[session['token']].empty():	
				requests.post(url, data=list(mapaCola[session['token']].queue)[0], headers=headers)
				mapaCola[session['token']].get()
			return redirect(url_for('mensajes'))
		except ConnectionError:
			return redirect(url_for('mensajes'))
	else:
		error = ""
		mensajes={}
		try:
			url = 'http://localhost:5001/mensajes'
			response = requests.get(url, headers=headers)
			mensajes = response.json()
		except ConnectionError:
			error = "Error de conexion"
		return render_template('mensajes.html', error = error, mensajes = mensajes)
#-------------------------------#


#-------------LOGIN-------------#
@app.route('/login', methods=['POST', 'GET'])
def login():

	if request.method == 'POST':
		try: 
			url = 'http://localhost:5001/usuario/'+request.form['nombre']
			response = requests.get(url)
			usuario_id = str(response.json()['id'])
			url = 'http://localhost:5001/usuario/'+usuario_id+'/'+request.form['password']
			response = requests.get(url)
			session.clear()
			session['nombre'] = request.form['nombre']
			session['token'] = response.json()['token']
			return redirect(url_for('index'))
		except ConnectionError:
			redirect(url_for('login'))
	else:
		return render_template('login.html')
#-------------------------------#


#-----------REGISTRAR-----------#
@app.route('/registrar', methods=['POST', 'GET'])
def registrar():

	if request.method == 'POST':
		try:
			payload = {'nombre':request.form['nombre'], 'password':request.form['password']}
			url = 'http://localhost:5001/usuario'
			requests.post(url, data=payload)
			return redirect(url_for('login'))
		except ConnectionError:
			redirect(url_for('registrar'))
	else:
		return render_template('registrar.html')
#-------------------------------#


#------------LOGOUT-------------#
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))
#-------------------------------#


#------------------------------MAIN------------------------------#
if __name__ == '__main__':
	app.run()
#----------------------------------------------------------------#
