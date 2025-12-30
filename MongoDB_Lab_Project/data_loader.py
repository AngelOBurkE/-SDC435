#Angelo Burke
#2.3 GP MongoDB Integration
#December 29, 2025
import json

def load_commits(file_path, mongo_mgr): 
    with open(file_path, "r", encoding="utf-8") as f: 
        data = json.load(f) 

    for commit in data: 
        mongo_mgr.add_commit(commit) 
  
    print("Commit data loaded into MongoDB.") 

def load_game_repos(file_path, mongo_mgr): 
    with open(file_path, "r", encoding="utf-8") as f: 
        data = json.load(f) 

    for repo in data: 
        mongo_mgr.add_repo(repo) 

    print("Game repository data loaded into MongoDB.")
