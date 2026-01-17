#Angelo Burke
#4.3 GP Neo4j integration
#Jan 17, 2026
import json 
def load_commits(file_path, neo_mgr): 
    with open(file_path, "r", encoding="utf-8") as f: 
        for line in f: 
            if line.strip(): 
                commit = json.loads(line) 
                username = commit.get("author", {}).get("name", "unknown") 
                repo = commit.get("repo", "unknown") 
                language = commit.get("language", "Unknown") 
                neo_mgr.add_commit(username, repo, language) 
    print("Commit data loaded into Neo4j.") 
