from pymongo import MongoClient
from flask import Flask,request,abort
from os import getenv
from dotenv import load_dotenv
load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)
app = Flask(__name__)

@app.route('/')
def index():
        try:
                phone = str(request.args.get("email"))
        except:
                return "'email' parameter was not specified",404
        phone = str(request.args.get("email"))
        #client = MongoClient("mongodb://localhost:27017/")
        database = client["xade"]
        phones = database["users"]
        try:
                phoneDetails = phones.find_one({"Email":str(phone)})
        except:
                print(e)
                return f"Email Address was not found",404
        phoneDetails = phones.find_one({"Email":str(phone)})
        if phoneDetails == None:
            return "Email Address was not found",404
        uid = phoneDetails["ID"]
        wallets = database["wallets"]
        try:
                walletDetails = wallets.find_one({"id":uid})
        except:
                return "Wallet Address was not found",404
        walletDetails = wallets.find_one({"ID":uid})
        return walletDetails["Wallet Address"],200

if __name__ == '__main__':
        app.run('127.0.0.1',8006)
