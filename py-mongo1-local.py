import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['PyDB_Local']
print (database)

# calling this collection "employees":
collection = database['employees'] 
print (collection)

# find employees
employees = collection.find()
print (employees)

# print employees 
for employee in employees:
    print(employee)
