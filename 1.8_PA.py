# Angelo Burke
# 1.8 PA Python Application Accessing
# December 18, 2025
# Purpose: Shows a CRUD operations using a Redis database
import redis 
  
# Connect to Redis server 
r = redis.Redis(host='localhost', port=6379, db=0) 

# CREATE: Add a new set 
def add_set(): 
    key = input("\nEnter the key you wish to add:\n") 
    count = int(input("\nEnter how many members will this set have:\n")) 
    for i in range(count): 
        member = input("\nEnter the next member value:\n") 
        r.sadd(key, member) 

# READ: Query set members 
def query_set(): 
    key = input("\nEnter the key you wish to query:\n") 
    members = r.smembers(key) 
    if members: 
        print("\nSet Members:") 
        for m in members: 
            print(m) 
    else: 
        print("\nSet does not exist or has no members.") 
 
# UPDATE: Modify set members 
def update_set(): 
    key = input("\nEnter the key of the set you wish to update:\n") 
    while True: 
        print("\nPlease type in a number and press enter to execute the menu option") 
        print("1. Add new member") 
        print("2. Remove member") 
        print("3. Remove all members") 
        print("4. Exit Update Menu") 

        choice = input() 
        if choice == "1": 
            member = input("\nEnter member to add:\n") 
            r.sadd(key, member) 
        elif choice == "2": 
            member = input("\nEnter member to remove:\n") 
            r.srem(key, member) 
        elif choice == "3": 
            print("\nRemoving all set members...") 
            members = r.smembers(key) 
            for m in members: 
                print(f"Removing Member: {m}...") 
                r.srem(key, m) 
            print("The cardinality of the set is now:") 
            print(r.scard(key)) 
        elif choice == "4": 
            break 
        else: 
            print("Invalid option.") 
  
# DELETE: Delete a set 
def delete_set(): 
    key = input("\nEnter the key of the set you wish to delete:\n") 
    r.delete(key) 
    print("Set deleted.") 
  
# DELETE ALL: Flush database 
def delete_all(): 
    r.flushall() 
    print("\nAll data removed from the database.") 
 
# MAIN MENU 
def main(): 
    while True: 
        print("\nType in a number and press enter to execute the menu option.") 
        print("1. Query for set members") 
        print("2. Add a new set") 
        print("3. Update members of a set") 
        print("4. Delete a set") 
        print("5. Delete all data from the database") 
        print("6. Exit the program") 
  
        choice = input() 
        if choice == "1": 
            query_set() 
        elif choice == "2": 
            add_set() 
        elif choice == "3": 
            update_set() 
        elif choice == "4": 
            delete_set() 
        elif choice == "5": 
            delete_all() 
        elif choice == "6": 
            break 
        else: 
            print("Invalid selection.") 

main()
