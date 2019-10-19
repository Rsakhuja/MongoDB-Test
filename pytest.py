import pymongo



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
    
    # Abstraction for DB
    db = client.DressesDB

    # Now connect with collection
    records = db.users

    # Get the count
    count = records.count_documents({})

    print('count=',count)

    GetOne(client, 'ridhima')
except pymongo.errors.ConnectionFailure:
    print("exception")








