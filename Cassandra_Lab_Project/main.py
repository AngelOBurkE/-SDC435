#Angelo Burke
#3.3 Project
#January 1, 2026
from cassandra_manager import CassandraManager
from data_loader import load_commits
from features import trending_repos, common_commit_words, commits_by_author 

def menu():
    print("\n--- GitHub Archive (Cassandra) ---")
    print("1. Load commit data")
    print("2. View commits by repo")
    print("3. Update commit message")
    print("4. Delete commit")
    print("5. Trending repositories")
    print("6. Common commit words")
    print("0. Exit") 

def main():
    cass_mgr = CassandraManager() 

    while True: 
        menu() 
        choice = input("Select option: ") 
 
        if choice == "1": 
            load_commits("data/Sample_Commits.json", cass_mgr) 
 
        elif choice == "2": 
            repo = input("Repository name: ") 
            commits = cass_mgr.get_commits_by_repo(repo) 
            for c in commits: 
                print(c.commit_id, "-", c.message) 
 
        elif choice == "3": 
            repo = input("Repo: ") 
            cid = input("Commit ID: ") 
            msg = input("New message: ") 
            cass_mgr.update_commit_message(repo, cid, msg) 
 
        elif choice == "4": 
            repo = input("Repo: ") 
            cid = input("Commit ID: ") 
            cass_mgr.delete_commit(repo, cid) 
 
        elif choice == "5": 
            commits = cass_mgr.session.execute("SELECT * FROM commits") 
            trending_repos(commits) 
 
        elif choice == "6": 
            commits = cass_mgr.session.execute("SELECT * FROM commits") 
            common_commit_words(commits) 
 
        elif choice == "0": 
            break 
 
        else: 
            print("Invalid option.") 
 
if __name__ == "__main__":
    main() 
