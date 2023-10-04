# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World"

# app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f"{num1} + {num2} = {result}"

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    result = num1 - num2
    return f"{num1} - {num2} = {result}"

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f"{num1} * {num2} = {result}"

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    result = num1 / num2
    return f"{num1} / {num2} = {result}"

app.run(debug=True)