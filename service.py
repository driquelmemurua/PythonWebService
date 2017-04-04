from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)

def validate_login(form):
	success = False

	return success

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		if validate_login(request.form):
			return redirect(url_for('chat'))
		else:
			abort(400)
	else: 
		return render_template('login.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(400)
def invalid_login(error):
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')