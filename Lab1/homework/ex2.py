from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()

post_collection = db["posts"]

new_post = {
    "title": "C4E25",
    "author": "AnhDD",
    "content": "Best "
}

post_collection.insert_one(new_post)
client.close()