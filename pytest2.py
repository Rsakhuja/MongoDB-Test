import pymongo

sample_dress = {
    'dressnumber': 1,
    'type': 'jeans',
    'color': 'green',
    'fabric': 'denims',
    'store': 'macys',
    'datebought': '10/19/2019',
    'pictures': ['a', 'b']
}


def CreateUser(client, username, age, email):
    data = {'userid': username, 'age': age, 'email': email}
    db = client.DressesDB
    collection = db.users
    
    recvd = collection.insert_one(data)
    print(recvd) 

def GetOne(client, userid):
    filter = {'userid': userid}
    db = client.DressesDB
    collection = db.users
    records = collection.find(filter)

    for document in records:
        print(document)


# mongodb+srv://admin:admin123@cluster0-46e5h.mongodb.net/dresses?retryWrites=true&w=majority
try:
    # Object represents a connection to the DB
    client = pymongo.MongoClient("mongodb://admin:admin123@cluster0-shard-00-00-46e5h.mongodb.net:27017,cluster0-shard-00-01-46e5h.mongodb.net:27017,cluster0-shard-00-02-46e5h.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

    CreateUser(client, 'adam', 32, 'john@gmail.com')
except pymongo.errors.ConnectionFailure:
    print("exception")