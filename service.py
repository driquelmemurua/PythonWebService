from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		return 'Hello, World'
	else: 
		return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')