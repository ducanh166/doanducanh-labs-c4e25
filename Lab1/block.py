uri = "mongodb://admin:admin1@ds137550.mlab.com:37550/c4e25"
from pymongo import MongoClient
import datetime
#1. connect to mLab server
client = MongoClient(uri)
#2. get a database
db = client.get_database()
#3. get a collection
post_collection = db["posts"]
#4. create a document
my_post = {
    "title": "Mat troi chan ly choi qua tim",
    "content": "Toi o nha code"
}
#lazy loading 
#5. insert document
#post_collection.insert_one(my_post) #lenh duy nhat de them du lieu vao database
for post in post_collection.find():
    print(post)
#first_post = my_post[1] # lấy dữ liệu từng cái 
for p in my_post:
    print(p)
#close connection
client.close()