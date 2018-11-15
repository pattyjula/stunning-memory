'''
DESC: connect to a MongoDB create a collection and
populate with content from a csv file, 2nd print
documents
'''

# import libraries
import pandas as pd
from pymongo import MongoClient
import json
import pprint
from pprint import PrettyPrinter

'''
DESC: connect to a MongoDB create a collection and
populate with content from a csv file, 2nd print
documents
'''

# specify variables
'''
Connection URL
server
mongo_con = MongoClient('mongodb://user:pwd@server:27017')
local uses localhost or maybe 127.0.0.1
mongo_con = MongoClient('mongodb://localhost:27017')
'''
mongo_con = MongoClient('mongodb://user:pwd@server:27017')
# collection
coll_name = ''
db_name='pjula'
database = mongo_con[db_name]

# Mongo will create collection if it does not exist
coll_name=database['crime']
# csv file to import
csv_path='staging/compStat_crime_draft.csv'


# list collections and create
# target collection if it doesn't exist
collist = database.list_collection_names()
# Check for collection and create
# if it doesn't exist
if "crime" in collist:
	print("The collection exists.")
else:
	coll_name = database["crime"]
	

def mongoimport(csv_path, db_name, coll_name):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    client = mongo_con
    db = client[db_name]
    print(client)
    coll = coll_name
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    print(coll.count())

# Run function to create database
mongoimport(csv_path, db_name, coll_name)

def mongoshow(db_name, coll_name):
    """ Connects to a client and pretty prints output
    """
    client = mongo_con
    db = client[db_name]
    coll = coll_name
	# specify limiter to keep output a certain length
    cursor = coll.find({}).limit(2)
    for document in cursor: 
        #pp = pprint.PrettyPrinter(depth=1)
        pprint.pprint(document, depth=1)

# Run function to show documents in collection
# mongoshow(db_name, coll_name)
