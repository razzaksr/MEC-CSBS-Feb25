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
    

def updateTransactions():
    print("Update transaction date by sender ")
    sender = input("enter the sender name ")
    newDate = input("Enter the new date ")
    condition = {"from":sender}
    modify = {"$set":{"date":newDate}}
    collection.update_many(condition,modify)
    print("Date of ",sender,"has updated")
    
def deleteTransactions():
    print("Deletion by date ")
    held = input("Enter the date to delete ")
    collection.delete_many({"date":held})
    print("transactions deleted @",held)
    
# main section >> menu driven interactions
print("welcome to transaction management system")



while True:
    print("1. Make new transaction")
    print("2. View Transaction")
    print("3. Update Transaction")
    print("4. Delete ")
    print("Any to logout")
    choice = int(input("Enter the choice "))
    if choice==1: newTrasnactions()
    elif choice==2: viewTransactions()
    elif choice==3: updateTransactions()
    elif choice==4: deleteTransactions()
    else: 
        print("logging out")
        break