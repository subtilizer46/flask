from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__,static_url_path='/static')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add',methods=['GET', 'POST'])
def add():
    create_table()

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        id = request.form['id']

        insert_table(username, email, id)
    return render_template('add.html')


@app.route('/delete',methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        id1 = request.form['id']
        delete_record(id1)
    return render_template('delete.html')

@app.route('/update',methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        id = request.form['id']

        update_table(username, email, id)
    return render_template('update.html')


@app.route('/display',methods=['GET', 'POST'])
def display():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM emp")
    data = cursor.fetchall()
    conn.close()
    return render_template('display.html', data=data)



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