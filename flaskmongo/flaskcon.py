from flask import Flask
import pymongo

app = Flask(__name__)

# MongoDB configuration
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'infy'

# Initialize MongoDB client and database
mongo_client = pymongo.MongoClient(
    host=app.config['MONGO_HOST'],
    port=app.config['MONGO_PORT']
)
db = mongo_client[app.config['MONGO_DBNAME']]

@app.route('/')
def index():
    if db is not None:
        return "Connected to MongoDB!"
    else:
        return "Failed to connect to the database."

if __name__ == '__main__':
    app.run()