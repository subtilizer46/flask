import pymongo

uri="mongodb://localhost:27017/"

client=pymongo.MongoClient(uri)

db=client.infy

connection=db.employee

if db is not None:
    print("Connected")