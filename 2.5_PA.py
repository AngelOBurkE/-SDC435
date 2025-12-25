#Name: Angelo Burke 
#Date: December 24, 2025 
#Assignment: 2.5 PA 
from pymongo import MongoClient 
from bson.objectid import ObjectId 
  
# ------------------------------------------------- 
# Connect to MongoDB 
# ------------------------------------------------- 
print("Connecting to local Mongo database...") 
client = MongoClient("mongodb://localhost:27017") 
db = client["Amazon"] 
collection = db["ReviewData"] 
print("Connection successful!") 
  
# ------------------------------------------------- 
# Menu Functions 
# ------------------------------------------------- 
def query_menu(): 
    print("\nPlease type in a number and press enter to execute the menu option") 
    print("1. Query by review_id") 
    print("2. Filter for a number of stars and greater") 
    print("3. Filter for less than a number of stars") 
    print("4. Filter for a word in the title") 
    print("5. Filter for a word in the review body") 
    choice = input("> ") 
    if choice == "1": 
        rid = input("Enter review_id: ") 
        doc = collection.find_one({"review_id": rid}) 
        print(doc) 
  
    elif choice == "2": 
        stars = input("Enter minimum number of stars: ") 
        results = collection.find({"stars": {"$gte": stars}}) 
        for doc in results: 
            print(doc) 
  
    elif choice == "3": 
        stars = input("Enter maximum number of stars: ") 
        results = collection.find({"stars": {"$lt": stars}}) 
        for doc in results: 
            print(doc) 
  
    elif choice == "4": 
        word = input("Search the title for: ") 
        results = collection.find({"review_title": {"$regex": word, "$options": "i"}}) 
        for doc in results: 
            print(doc) 
  
    elif choice == "5": 
        word = input("Search the review body for: ") 
        results = collection.find({"review_body": {"$regex": word, "$options": "i"}}) 
        for doc in results: 
            print(doc)
            
def add_document(): 
    print("\nAdd a New Document") 
    new_doc = { 
        "review_id": input("Review ID: "), 
        "product_id": input("Product ID: "), 
        "reviewer_id": input("Reviewer ID: "), 
        "stars": input("Stars: "), 
        "review_body": input("Review Body: "), 
        "review_title": input("Review Title: "), 
        "language": input("Language: "), 
        "product_category": input("Product Category: ") 
    } 
    collection.insert_one(new_doc) 
    print("Document added successfully!") 
  
def update_document(): 
    rid = input("What is the ReviewID you wish to update? ") 
    field = input("Which field would you like to update? ") 
    new_value = input("What would you like to change the value to? ") 
    collection.update_one( 
        {"review_id": rid}, 
        {"$set": {field: new_value}} 
    ) 
  
    updated_doc = collection.find_one({"review_id": rid}) 
    print("New document has been updated to:") 
    print(updated_doc) 
  
def delete_document(): 
    rid = input("What is the ReviewID of the document you wish to delete? ") 
    collection.delete_one({"review_id": rid}) 
    print("Document deleted!") 
  
def delete_all_documents(): 
    confirm = input("Are you sure you want to delete ALL documents? (yes/no): ") 
    if confirm.lower() == "yes": 
        collection.delete_many({}) 
        print("All documents deleted.") 
  
def delete_collection(): 
    confirm = input("Are you sure you want to delete the collection? (yes/no): ") 
    if confirm.lower() == "yes": 
        db.drop_collection("ReviewData") 
        print("Collection deleted.") 
  
# ------------------------------------------------- 
# Main Menu Loop 
# ------------------------------------------------- 
while True: 
    print("\nType in a number and press enter to execute the menu option.") 
    print("1. Query for documents") 
    print("2. Add a new document") 
    print("3. Update fields of a document") 
    print("4. Delete a document") 
    print("5. Delete all documents from the collection") 
    print("6. Delete a collection") 
    print("7. Exit the program") 
  
    option = input("> ") 
    if option == "1": 
        query_menu() 
    elif option == "2": 
        add_document() 
    elif option == "3": 
        update_document() 
    elif option == "4": 
        delete_document() 
    elif option == "5": 
        delete_all_documents() 
    elif option == "6": 
        delete_collection() 
    elif option == "7": 
        print("Exiting program...") 
        break 
    else: 
        print("Invalid option. Please try again.") 
