#Angelo Burke
#4.3 GP Neo4j integration
#Jan 17, 2026
from neo4j_manager import Neo4jManager
from data_loader import load_commits
from features import show_user_repos, repos_by_language, most_active_users 

def menu():
    print("\n--- GitHub Archive (Neo4j) ---")
    print("1. Load commit data")
    print("2. View user repositories")
    print("3. Update repository name")
    print("4. Delete repository")
    print("5. Repositories by language")
    print("6. Most active users")
    print("0. Exit") 

def main(): neo_mgr = Neo4jManager(
    "bolt://localhost:7687",
    "neo4j",
    "Password1"
    ) 

while True: 
   menu() 
   choice = input("Select option: ") 
 
   if choice == "1": 
       load_commits("data/Sample_Commits.json", neo_mgr) 
 
   elif choice == "2": 
       show_user_repos(neo_mgr) 
 
   elif choice == "3": 
       old = input("Old repo name: ") 
       new = input("New repo name: ") 
       neo_mgr.update_repo_name(old, new) 
 
   elif choice == "4": 
       repo = input("Repo to delete: ") 
       neo_mgr.delete_repo(repo) 
 
   elif choice == "5": 
       repos_by_language(neo_mgr) 
 
   elif choice == "6": 
       most_active_users(neo_mgr) 
 
   elif choice == "0": 
       neo_mgr.close() 
       break 
 
   else: 
       print("Invalid option.") 
 
if name == "main": main() 
