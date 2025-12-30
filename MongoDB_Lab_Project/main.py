#Angelo Burke
#2.3 GP MongoDB Integration
#December 29, 2025
from mongo_manager import MongoManager
from data_loader import load_commits, load_game_repos
from features import (
    message_length_survey,
    watch_distribution,
    popular_commit_words
)

def menu():
    print("\n--- MongoDB GitHub Archive ---")
    print("1. Load commit data (github_commits.json)")
    print("2. View commits by author")
    print("3. Update watch count")
    print("4. Delete commits by author")
    print("5. Message length survey")
    print("6. Watch count distribution")
    print("7. Popular commit words")
    print("8. Load game repositories (optional)")
    print("0. Exit") 

def main():
    mongo_mgr = MongoManager()
    while True:
        menu()
        choice = input("Select an option: ") 
 
        if choice == "1": 
            load_commits("data/github_commits.json", mongo_mgr) 
 
        elif choice == "2": 
            name = input("Author name: ") 
            results = mongo_mgr.get_commits_by_author(name) 
            for r in results: 
                print(r) 
 
        elif choice == "3": 
            name = input("Author name: ") 
            count = int(input("New watch count: ")) 
            mongo_mgr.update_watch_count(name, count) 
 
        elif choice == "4": 
            name = input("Author name: ") 
            mongo_mgr.delete_commits_by_author(name) 
 
        elif choice == "5": 
            message_length_survey(mongo_mgr) 
 
        elif choice == "6": 
            watch_distribution(mongo_mgr) 
 
        elif choice == "7": 
            popular_commit_words(mongo_mgr) 
 
        elif choice == "8": 
            load_game_repos("data/game_repos.json", mongo_mgr) 
 
        elif choice == "0": 
            break 
 
        else: 
            print("Invalid option.") 
 
if __name__ == "__main__":
    main() 
