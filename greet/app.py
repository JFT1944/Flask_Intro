from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome'
@app.route('/welcome/home')
def welcomehome():
    return 'Welcome Home'
@app.route('/welcome/back')
def welcomeback():
    return 'Welcome Back'
@app.route('/')
def homepage():
    return "you on the homepage mudda fukka"