#Angelo Burke
#3.3 Project
#January 1, 2026
from cassandra.cluster import Cluster 
class CassandraManager:
    def init(self):
        self.cluster = Cluster(["127.0.0.1"])
        self.session = self.cluster.connect("github") 

    # CREATE 
    def add_commit(self, repo, commit_id, author, message): 
        query = """ 
        INSERT INTO commits (repo_name, commit_id, author, message) 
        VALUES (%s, %s, %s, %s) 
        """ 
        self.session.execute(query, (repo, commit_id, author, message)) 
 
    # READ 
    def get_commits_by_repo(self, repo): 
        query = "SELECT * FROM commits WHERE repo_name=%s" 
        return self.session.execute(query, (repo,)) 
 
    # UPDATE 
    def update_commit_message(self, repo, commit_id, message): 
        query = """ 
        UPDATE commits 
        SET message=%s 
        WHERE repo_name=%s AND commit_id=%s 
        """ 
        self.session.execute(query, (message, repo, commit_id)) 
 
    # DELETE 
    def delete_commit(self, repo, commit_id): 
        query = "DELETE FROM commits WHERE repo_name=%s AND commit_id=%s" 
        self.session.execute(query, (repo, commit_id)) 
