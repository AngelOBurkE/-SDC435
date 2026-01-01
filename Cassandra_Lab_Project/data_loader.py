#Angelo Burke
#3.3 Project
#January 1, 2026
import json 
  
def load_commits(file_path, cass_mgr): 
    with open(file_path, "r", encoding="utf-8") as f: 
        for line in f: 
            if line.strip():
                commit = json.loads(line) 
  
                repo = commit.get("repo", "unknown") 
                commit_id = commit.get("id", "no_id") 
                author = commit.get("author", {}).get("name", "unknown") 
                message = commit.get("message", "") 
  
                cass_mgr.add_commit(repo, commit_id, author, message) 
    print("Commits loaded into Cassandra.") 
