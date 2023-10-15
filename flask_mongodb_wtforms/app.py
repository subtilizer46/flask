from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from wtforms import StringField, Form

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"

mongo = PyMongo(app)

class UserForm(Form):
    name = StringField('Name')

@app.route('/')
def index():
    users = mongo.db.users.find()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        mongo.db.users.insert_one({'name': name})
        flash('User added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    name = request.form.get('name')
    mongo.db.users.update_one({'_id': ObjectId(user_id)}, {"$set": {'name': name}})
    flash('User updated successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    flash('User deleted successfully!', 'success')
    return redirect(url_for('index'))

from bson.objectid import ObjectId  # Required to convert string representation of ObjectId to actual ObjectId

if __name__ == "__main__":
    app.run(debug=True)