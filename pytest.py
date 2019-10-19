import pymongo

# mongodb+srv://admin:admin123@cluster0-46e5h.mongodb.net/dresses?retryWrites=true&w=majority
try:
    # myclient = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0-46e5h.mongodb.net/DressesDB?retryWrites=true&w=majority")


    client = pymongo.MongoClient("mongodb://admin:admin123@cluster0-shard-00-00-46e5h.mongodb.net:27017,cluster0-shard-00-01-46e5h.mongodb.net:27017,cluster0-shard-00-02-46e5h.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    

    # client = pymongo.MongoClient('mongodb+srv://admin:admin123@cluster0-46e5h.mongodb.net/test?retryWrites=true&w=majority')
    db = client.DressesDB

    # db = client.get_database('DressesDB')

    records = db.dresses

    count = records.count_documents({})

    print(count)

except pymongo.errors.ConnectionFailure:
    print("exception")


print(client)






