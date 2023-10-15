## Microservices(L5)

1. Write a basic Flask application that returns "Hello, World!" on the root route.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

```
  
2. Add a route `/greet/<name>` to greet a user by their name.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>', methods=['GET'])
def greet_user(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run()

```

3. Write a Flask route that accepts a query parameter `age` and returns whether the user is an adult or minor.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/check-age<age>')
def check_age(age):
    if int(age) >= 18:
        return "You are an adult."
    else:
        return "You are a minor."


if __name__ == '__main__':
    app.run()

```

4. Create a Flask route that accepts POST requests and returns the JSON data received.
```python
from flask import request, jsonify

app = Flask(__name__)


@app.route('/post-data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()

```

5. How would you implement basic authentication for a Flask route?
```python
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'your_username'
app.config['BASIC_AUTH_PASSWORD'] = 'your_password'
basic_auth = BasicAuth(app)

@app.route('/secure-route')
@basic_auth.required
def secure_route():
    return "This route is protected with basic authentication."

```

6. Write a route that returns the user agent of the request.
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/user-agent')
def get_user_agent():
    user_agent = request.user_agent.string
    return f"User Agent: {user_agent}"


if __name__ == '__main__':
    app.run()

```

7. Implement a route `/add` that takes two query parameters, `a` and `b`, and returns their sum.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:a>/<int:b>')
def add_numbers(a,b):
    result = a + b
    return f"The sum of {a} and {b} is {result}."

if __name__ == '__main__':
    app.run()

```

8. Use Flask's `Blueprint` to organize routes related to `products`.
```python
from flask import Flask

app = Flask(__name__)

categories = Blueprint('categories', __name__)

@categories.route('/')
def category_list():
    return "List of categories"

app.register_blueprint(categories, url_prefix='/categories')

if __name__ == '__main__':
    app.run()
```

9. Create a simple REST API for CRUD operations on a `Todo` entity.
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todos.append(data)
    return jsonify({'message': 'Todo created successfully'})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    if id < len(todos):
        return jsonify(todos[id])
    else:
        return jsonify({'error': 'Todo not found'}), 404

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    if id < len(todos):
        todos[id] = data
        return jsonify({'message': 'Todo updated successfully'})
    else:
        return jsonify({'error': 'Todo not found'}), 404

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    if id < len(todos):
        del todos[id]
        return jsonify({'message': 'Todo deleted successfully'})
    else:
        return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run()

```

10. Write middleware in Flask that logs each request's method and path.
```python
from flask import Flask, request

app = Flask(__name__)

def log_request_info():
    method = request.method
    path = request.path
    app.logger.info(f"Request: {method} {path}")

app.before_request(log_request_info)

@app.route('/')
def hello_world():
    return "Hello!!!"

if __name__ == '__main__':
    app.run()
```