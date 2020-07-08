import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['PyDB_Local']
print (database)

# calling this collection "students":
collection = database['employees'] 
print (collection)

# insert one document
doc = {'first_name': 'Peter', 'last_name': 'Smith', 
 'email': 'peters@email.ca', 'job_title': 'clerk', 
 'hire_date': '2000-01-10', 'salary': 20000}

collection.insert_one(doc)

# insert many documents
multi_doc = [{'first_name': 'Amy', 'last_name': 'Clark', 
 'email': 'amyc@email.ca', 'job_title': 'designer', 
 'hire_date': '2001-02-03', 'salary': 40000},
 {'first_name': 'Viola', 'last_name': 'Che', 
 'email': 'voilac@email.ca', 'job_title': 'developer', 
 'hire_date': '2001-02-10', 'salary': 35000},
{'first_name': 'Vicky', 'last_name': 'Williams', 
 'email': 'vickyw@email.ca', 'job_title': 'manager', 
 'hire_date': '2000-01-05', 'salary': 50000}]

collection.insert_many(multi_doc)

# find employees
employees = collection.find()

# print employees
for employee in employees:
    print(employee)

