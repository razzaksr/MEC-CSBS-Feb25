from pymongo import *
url = "mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# create connection between python and mongo atlas
client = MongoClient(url)
# refer the muthayammal database in my cluster
database = client.muthayammal
# refer the collection name transactions from muthayammal database
collection = database.transactions

# read
def viewTransactions():
    for x in collection.find():
        print(x)

# insert new document
def newTrasnactions():
    print("user must provide following details")
    date = input("Enter the date of transaction")
    sender = input("Enter the sender name ")
    receiver = input("Enter the receiver name ")
    amount = int(input("Enter the amount "))
    types = input("Enter the type of transaction ")
    document = {"date":date,"from":sender,
                "to":receiver,"amount":amount,
                "type":types}
    collection.insert_one(document)
    print("Transaction done")
# main section
newTrasnactions()
viewTransactions()
