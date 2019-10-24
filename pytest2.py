import pymongo

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


# Setup the client connection to the DB
try:
    # Object represents a connection to the DB
    client = pymongo.MongoClient("mongodb://admin:admin123@cluster0-shard-00-00-46e5h.mongodb.net:27017,cluster0-shard-00-01-46e5h.mongodb.net:27017,cluster0-shard-00-02-46e5h.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    # CreateUser(client, 'adam1', 32, 'john@gmail.com')
    GetOne(client,'rina')
except pymongo.errors.ConnectionFailure:
    print("exception")
