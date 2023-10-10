from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'infy'

client = pymongo.MongoClient(
    host=app.config['MONGO_HOST'],
    port=app.config['MONGO_PORT']
)

db = client[app.config['MONGO_DBNAME']]
collection=db['menu']

@app.route('/create', methods=['POST'])
def create_document():
    collection.insert_one(data)
    return jsonify(message="Document inserted successfully!")

@app.route('/read', methods=['GET'])
def read_documents():
    documents = collection.find()
    result = []
    for doc in documents:
        result.append(doc)
    return jsonify(result)

@app.route('/update', methods=['PUT'])
def update_document():
    update_query = request.json.get("query")
    new_data = request.json.get("new_data")
    collection.update_one(update_query, {"$set": new_data})
    return "Document updated successfully!"

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_document():
    collection.delete_one(id)
    return "Document deleted successfully!"

if __name__ == '__main__':
    app.run(debug=True)