#Angelo Burke
#2.3 GP MongoDB Integration
#December 29, 2025
from pymongo import MongoClient 

class MongoManager:
    def init(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["GitHubArchive"]
        elf.commits = self.db["Commits"]
        self.repos = self.db["GameRepos"] 

    def add_commit(self, commit):
       self.commits.insert_one(commit) 
 
    def get_commits_by_author(self, name): 
       return list(self.commits.find({"author.name": name})) 
 
    def update_watch_count(self, author, count): 
       self.commits.update_many( 
           {"author.name": author}, 
           {"$set": {"watch_count": count}} 
       ) 
 
    def delete_commits_by_author(self, author): 
       self.commits.delete_many({"author.name": author}) 
