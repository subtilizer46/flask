from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run()