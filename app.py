from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operation](a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)

def add(a, b):
    """Add a and b."""
    return a + b

def sub(a, b):
    """Subtract b from a."""
    return a - b

def mult(a, b):
    """Multiply a and b."""
    return a * b

def div(a, b):
    """Divide a by b."""
    return a / b

