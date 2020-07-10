import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['PyDB_Local']
print (database)

# calling this collection "employees":
collection = database['employees'] 
print (collection)

# find employees
employees = collection.find()

# display menu and accept option
def display_options():
    print("")
    print("1. Add a record")
    print("2. View a record")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    print("")
    user_option = input("Enter option number: ")
    return user_option

# Create function for CRUD
def add_record(): 
    print("") 
    # assign variable for the input values
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    email = input("Enter the email: ")
    title = input("Enter the job title: ")
    hire_date = input("Enter the hire date: ")
    salary = input("Enter the salary (Default 0): ")
    if salary.isnumeric():
        salary = int(salary)
    else:
        salary = 0

    new_doc = { 
        "first_name": first.lower(),
        "last_name": last.lower(),
        "email": email.lower(),
        "title": title.lower(),
        "hire_date": hire_date,
        "salary": salary
    }

    # Create document 
    try:
        collection.insert_one(new_doc)
        print("")
        print("Document added")
    
     # The except block lets you handle the error.
    except:
        print("Error accessing the database")



def get_record():
    print("") # just to have a space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    try:
        doc = collection.find_one({'first_name':first.lower(), 'last_name':last.lower()})
        if not doc:
            print("")
            print("No result found.")
    except:
        print("Error accessing the database")
    return doc


def view_record():
    # Define a variable, which gets the result of our get_record() function
    doc = get_record()
    print("")
    if doc: # if we do have some results we will continue with printing the full record
        for key, value in doc.items():
            # In this loop we need to display all the keys and their values
            # except the id key 
            if key!="_id":  
                print(key.capitalize(),": ", value)   
                #if (isinstance(value,str)):
                #    print(key.capitalize(),": ", value.capitalize())    
                #else:
                #    print(key.capitalize(),": ", value)   


def del_record():
    doc = get_record() # getting the result from get_record() function
    if doc: # check if any result has been returned from get_record()
        print("")
        # iterate through the items of the returned doc and print (display) each of the values
        for key, value in doc.items():
            if key!="_id":
                print(key.capitalize(),": ", value)  
                #if (isinstance(value,str)):
                #    print(key.capitalize(),": ", value.capitalize())    
                #else:
                #    print(key.capitalize(),": ", value)  
        print("")
        confirm = input("Is this employee document you want to delete?\nY or N: ")
        print("")

        # Our if condition to perform the delete operation or just ignore it based on the user's input
        if confirm.lower()=='y':
            try:
                collection.delete_one(doc)
                print("")
                print("Document deleted")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")


def edit_record():
    doc = get_record()
    if doc: 
        # create an empty dictionary called "update_doc"
        update_doc = {} # to create a new empty doc
        print("")
         
        for key, value in doc.items():
        # filter out the ID field
            if key != "_id":    
                if key == "salary":
                    update_doc[key] = input(f"{key} [{value}]: ") # first [alex] : type any thing or just leave it empty
                    if update_doc[key] !="": 
                        if update_doc[key].isnumeric():
                            update_doc[key] = int(update_doc[key])
                        else:
                            update_doc[key] = value
                else:
                    update_doc[key] = input(f"{key} [{value}]: ").lower()

                if  update_doc[key]=="":
                    # reasign the current value to the same key again
                    update_doc[key] = value

        # for testing we will print the udpate_doc that contains all the values:
        print("") # Just printing a blank line
        print ("The new updated employee:")
        print ("=========================")
        for key, value in update_doc.items():
            print(key, ": [",value,"]")

        # update_one()
        # The pure update command example: db.users.update({first_name:"martin"},{ $set: {"last_name":"smith" }})
        # collection_name.update_one(doc, {'$set': update_doc})
        try:
            collection.update_one(doc, { '$set': update_doc})     
            # $set: the MongoDB keyword to set/write the new values
            # update_doc: the dictionary (object) that we're going to pass in, the one we have just created
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


# process option selected
def keep_asking():
    while True: 
        option = display_options()
        if option == "1":
            print("You have selected option 1 (Add a record)")
            add_record()
        elif option == "2":
            print("You have selected option 2 (View a record)")
            view_record()
        elif option == "3":
            print("You have selected option 3 (Edit a record)")
            edit_record()
        elif option == "4":
            print("You have selected option 4 (Delete a record)")
            del_record()
        elif option == "5":
            client.close()
            break
        else:
            print("Invalid Option!")


# 2: Call our function keep_asking()
keep_asking()


