import csv
from pymongo import MongoClient

f = open("scrap_code/mt_list100.csv", "r", encoding="utf-8")
readers = csv.reader(f)

# for reader in readers:
#     print(reader)

with MongoClient("mongodb://localhost:27017/") as client:
    mt_db = client["mt_db"]
    if "mt_collection" not in mt_db.list_collection_names():
        mt_db.create_collection('mt_collection')

    number = ""
    name = ""
    height = ""
    location = ""
    for reader in readers:
        number = reader[0]
        name = reader[1]
        height = reader[2]
        location = reader[3]
        
        data = {'number': number, 'name': name, 'height': height, 'location': location}
        mt_db.mt_collection.insert_one(data)

# 172.17.0.2