from flask import Flask,render_template

app=Flask(__name__)

@app.route('/signup')
def signup():
    return "Signup Page world!!!"

@app.route('/login')
def login():
    head="JINJA"
    return render_template('login.html',head=head)

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

app.run(debug=True)