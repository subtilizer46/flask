from flask import Flask, render_template
import sqlite3

app = Flask(__name__,static_url_path='/static')

@app.route('/home')
def home():
    create_table()
    cname = "India"
    p1="Home"
    p2="Contact"
    p3="Services"
    paragraph = "Welcome to Flask World !!"
    return render_template('home.html',cname=cname,p1=p1,p2=p2,p3=p3,paragraph=paragraph)

@app.route('/insert/<string:username>/<string:email>/<int:id>')
def insert(username,email,id):
    insert_table(username,email,id)
    return render_template('home.html')


@app.route('/delete/<int:id>')
def delete(id):
    delete_record(id)
    return render_template('home.html')

@app.route('/update/<string:username>/<string:email>/<int:id>')
def update(username,email,id):
    update_table(username,email,id)
    return render_template('home.html')

@app.route('/display')
def display():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM emp")
    data = cursor.fetchall()
    conn.close()
    return render_template('display.html', data=data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')


def create_table():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp(
                   id INTEGER,
                   username TEXT,
                   email TEXT

    )
""")
    conn.commit()
    conn.close()


def insert_table(new_username, new_email, id):
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp(id,username,email) VALUES (?,?,?)",(id, new_username, new_email))
    conn.commit()
    conn.close()

def update_table(new_username, new_email, id):
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE emp SET username = ?, email = ? WHERE id = ?", (new_username, new_email, id))
    conn.commit()
    conn.close()

def delete_record(id):
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emp WHERE id = ?", (id,))
    conn.commit()
    conn.close()

app.run(host='127.0.0.1', port=7000, debug=True)