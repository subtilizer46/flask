from flask import Flask, request

app = Flask(__name__)

@app.route('/user-agent')
def get_user_agent():
    user_agent = request.user_agent.string
    return f"User Agent: {user_agent}"


if __name__ == '__main__':
    app.run()