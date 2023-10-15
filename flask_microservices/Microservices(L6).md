## Microservices(L6)

11. Create a Flask route that sets a cookie named `user_id`.
```python
from flask import make_response

app = Flask(__name__)

@app.route('/set-cookie/<user_id>')
def set_cookie(user_id):
    resp = make_response("Cookie Set")
    resp.set_cookie('user_id', user_id)
    return resp

if __name__ == '__main__':
    app.run()

```
12. Write a Flask route that reads a cookie named `session_id`.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/read')
def read_cookie():
    session_id = request.cookies.get('session_id')
    if session_id:
        return f"Value of 'session_id' is: {session_id}"
    else:
        return "Cookie for 'session_id' not found."

if __name__ == '__main__':
    app.run()
```

13. How would you handle errors in Flask and return a custom error JSON response?
```python
from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

```

14. Create a route that accepts a file upload and saves it to the server.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/upload-file', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save('path/to/save/file')
        return 'File uploaded successfully'
    return 'No file provided'

if __name__ == '__main__':
    app.run()
```

15. Implement a route that returns a JSON list of users from an in-memory list.
```python
from flask import Flask

app = Flask(__name__)

users = [{'id': 1, 'name': 'rahul'}, {'id': 2, 'name': 'sahil'}]

@app.route('/get-users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run()
```

16. Write a Flask application that uses environment variables for configuration.
```python
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

@app.route('/')
def hello():
    return "Hello, World!"
```

17. Create a rate-limited route that allows only 5 requests per minute.
```python
from flask import Flask, request, jsonify
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/limited', methods=["GET"])
@limiter.limit("5 per minute")
def limited():
    return jsonify(success=True), 200
```

18. Implement a route `/reverse` that reverses the given string query parameter.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/reverse/<string:str>')
def reverse_string():
    if str:
        reversed_string = str[::-1]
        return f"Reversed string: {reversed_string}"
    return "Please provide a 'string' parameter."

if __name__ == '__main__':
    app.run()
```

19. Write a route that returns the current server time in a JSON response.
```python
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/current-time')
def current_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'current_time': current_time})

if __name__ == '__main__':
    app.run()

```

20. Create a route that returns a static HTML file.
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static')
def static_html():
    return render_template('static.html')

if __name__ == '__main__':
    app.run()

```