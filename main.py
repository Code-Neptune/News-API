import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DB = os.getenv("MONGODB_DB")
MONGODB_COL = os.getenv("MONGODB_COL")

def mongo_upload():
    myclient = pymongo.MongoClient(MONGODB_URL)

    try:
        my_newsdb = myclient[MONGODB_DB]
        my_dbcol = my_newsdb[MONGODB_COL]
        print(my_newsdb.list_collection_names())
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

mongo_upload()