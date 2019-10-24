import pymongo

sample_dress = {
    'dressnumber':1,
    'type':'jean',
    'color':'blue',
    'fabric':'denim',
    'store':'macys',
    'datebought':'10192019',
    'pictures':['a','b']
}

#Read Operation
def GetOne(client, userid):
    filter = {'userid': userid}
    db = client.DressesDB
    collection = db.users
    records = collection.find(filter)

    for document in records:
        print(document)
#Create Operation
def CreateOne(client, userid,age,email):
    post = {'userid':userid, 'age':age,'email':email}
    db = client.DressesDB
    collection = db.users
    new_post = collection.insert_one(post)

    filter = {'userid':userid}
    records = collection.find(filter)

    for document in records:
        print(document)

#Delete Operation
def DeleteOne(client, userid):
    filter = {'userid':userid}

    db = client.DressesDB
    collection = db.users

    collection.delete_one(filter)

#Update Operation
def UpdateOne(client,userid,param, newVal):
    findUserFilter = {'userid':userid}

    filter = {'$set':{param: newVal}}

    db = client.DressesDB
    collection = db.users

    collection.update_one(
        {'userid':userid},
        {'$set': {param: newVal}}
    )

# mongodb+srv://admin:admin123@cluster0-46e5h.mongodb.net/dresses?retryWrites=true&w=majority
try:
    # Object represents a connection to the DB
    client = pymongo.MongoClient("mongodb://admin:ridhima12@cluster0-shard-00-00-46e5h.mongodb.net:27017,cluster0-shard-00-01-46e5h.mongodb.net:27017,cluster0-shard-00-02-46e5h.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

    # Abstraction for DB
    db = client.DressesDB

    # Now connect with collection
    records = db.users

    # GetOne(client, 'ridhima')

    # CreateOne(client,'newCreate',23,'create@gmail.com')

    # DeleteOne(client,'ridhima')

    UpdateOne(client, 'rishika', 'age', 5)

    # Get the count
    count = records.count_documents({})

    print('count=',count)


except pymongo.errors.ConnectionFailure:
    print("exception")
