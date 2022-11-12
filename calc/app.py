# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <div>
        <form action="" method="">
            <input type="text" name="num1"></input>
            <input type="text" name="num2"></input>
            <button>multiply</button>
            <button type=""><a href="/div">Divide</a></button>
            <button>add</button>
            <button>subtract</button
        </form>    
    </div>
    '''
    
@app.route('/add')
def add():
    num1 = request.args['num1']
    num2 = request.args['num2']
    answer = int(num1) + int(num2)
    return str(answer)

@app.route('/sub')
def sub():
    num1 = request.args['num1']
    num2 = request.args['num2']
    answer = int(num1) - int(num2)
    return str(answer)

@app.route('/mult')
def multi():
    num1 = request.args['num1']
    num2 = request.args['num2']
    answer = int(num1) * int(num2)
    return str(answer)

@app.route('/div')
def div():
    num1 = request.args['num1']
    num2 = request.args['num2']
    answer = int(num1) / int(num2)
    return str(answer)
