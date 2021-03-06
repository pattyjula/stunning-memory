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

# specify variables
'''
Connection URL
server
mongo_con = MongoClient('mongodb://user:pwd@server:27017')
local uses localhost or maybe 127.0.0.1
'''
mongo_con = MongoClient('mongodb://localhost:27017')
db_name='patty'
database = mongo_con[db_name]
coll_name='weekly_crime_up'
csv_path='open_data_weekly_upload_occ_crm_data_i_u.csv'

collist = database.list_collection_names()
# Check for collection and create
# if it doesn't exist
if "weekly_crime_up" in collist:
	print("The collection exists.")
else:
	coll_name = database["weekly_crime_up"]
	

def mongoimport(csv_path, db_name, coll_name):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    #'10.200.14.135'
    client = mongo_con
    db = client[db_name]
    print(client)
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    print(coll.count())


mongoimport(csv_path,db_name, coll_name)

def mongoshow(db_name, coll_name):
    """ Connects to a client and pretty prints output
    """
    client = mongo_con
    db = client[db_name]
    coll = db[coll_name]
	# specify limiter to keep output a certain length
    cursor = coll.find({}).limit(2)
    for document in cursor: 
        #pp = pprint.PrettyPrinter(depth=1)
        pprint.pprint(document, depth=1)

#mongoshow(db_name, coll_name)

