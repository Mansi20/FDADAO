import json
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.drugs
record1 = db.drug_collection

page = open("../openFDA-human-drug/files/drug-event-0002-of-0033.json","r")
parsed = json.loads(page.read())

for item in parsed["results"]:
    print(item)
    record1.insert(item)

