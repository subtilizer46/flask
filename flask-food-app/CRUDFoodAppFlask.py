# from flask import Flask, request, jsonify
# import pymongo

# app = Flask(__name__)

# app.config['MONGO_HOST'] = 'localhost'
# app.config['MONGO_PORT'] = 27017
# app.config['MONGO_DBNAME'] = 'infy'

# client = pymongo.MongoClient(
#     host=app.config['MONGO_HOST'],
#     port=app.config['MONGO_PORT']
# )

# db = client[app.config['MONGO_DBNAME']]
# collection=db['menu']

# @app.route('/create', methods=['POST'])
# def create_document():
#     collection.insert_one(data)
#     return jsonify(message="Document inserted successfully!")

# @app.route('/read', methods=['GET'])
# def read_documents():
#     documents = collection.find()
#     result = []
#     for doc in documents:
#         result.append(doc)
#     return jsonify(result)

# @app.route('/update', methods=['PUT'])
# def update_document():
#     update_query = request.json.get("query")
#     new_data = request.json.get("new_data")
#     collection.update_one(update_query, {"$set": new_data})
#     return "Document updated successfully!"

# @app.route('/delete/<int:id>', methods=['DELETE'])
# def delete_document():
#     collection.delete_one(id)
#     return "Document deleted successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/infy'  # Update with your MongoDB URI
mongo = PyMongo(app)

# Create a collection for restaurants if it doesn't exist
if 'restaurants' not in mongo.db.list_collection_names():
    mongo.db.create_collection('restaurants')
    mongo.db.restaurants.insert_many([
        {
            'name': 'Restaurant 1',
            'cuisine': 'Italian',
            'location': 'City 1',
        },
        {
            'name': 'Restaurant 2',
            'cuisine': 'Mexican',
            'location': 'City 2',
        },
        # Add more restaurants as needed
    ])

# Create a collection for bookings if it doesn't exist
if 'bookings' not in mongo.db.list_collection_names():
    mongo.db.create_collection('bookings')

# Define routes and views
@app.route('/')
def index():
    restaurants = mongo.db.restaurants.find()
    return render_template('index.html', restaurants=restaurants)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/book/<restaurant_id>', methods=['GET', 'POST'])
def book(restaurant_id):
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        booking = {
            'restaurant_id': restaurant_id,
            'name': name,
            'date': date
        }
        mongo.db.bookings.insert_one(booking)
        return redirect(url_for('index'))
    else:
        return render_template('booking.html', restaurant_id=restaurant_id)

if __name__ == '__main__':
    app.run(debug=True)
