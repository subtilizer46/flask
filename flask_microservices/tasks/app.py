from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory store for tasks
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if not task:
        return jsonify({"error": "Task not provided"}), 400

    tasks.append(task)
    return jsonify({"message": "Task added!"}), 201

if __name__ == '__main__':
    app.run(port=5001)