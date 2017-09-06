import os
from flask import Flask,render_template, request,json
app = Flask("First App")

@app.route('/')
def index():
	return "Yes it is working"

@app.route('/next')
def next_route():
	return "Ohh Yes it is working"


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signupuser', methods=['POST'])
def signupuser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});



if __name__ == "__main__":
	app.run()
