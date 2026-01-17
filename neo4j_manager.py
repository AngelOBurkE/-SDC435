#Angelo Burke
#4.3 GP Neo4j integration
#Jan 17, 2026
from neo4j import GraphDatabase 

class Neo4jManager:
    def init(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password)) 

def close(self): 
   self.driver.close() 
 
# CREATE 
def add_commit(self, username, repo, language): 
   with self.driver.session() as session: 
       session.run(""" 
       MERGE (u:User {name: $username}) 
       MERGE (r:Repository {name: $repo}) 
       MERGE (l:Language {name: $language}) 
       MERGE (u)-[:COMMITTED_TO]->(r) 
       MERGE (r)-[:USES_LANGUAGE]->(l) 
       """, username=username, repo=repo, language=language) 
 
# READ 
def get_user_repos(self, username): 
   with self.driver.session() as session: 
       result = session.run(""" 
       MATCH (u:User {name: $username})-[:COMMITTED_TO]->(r) 
       RETURN r.name 
       """, username=username) 
       return [record["r.name"] for record in result] 
 
# UPDATE 
def update_repo_name(self, old_name, new_name): 
   with self.driver.session() as session: 
       session.run(""" 
       MATCH (r:Repository {name: $old}) 
       SET r.name = $new 
       """, old=old_name, new=new_name) 
 
# DELETE 
def delete_repo(self, repo): 
   with self.driver.session() as session: 
       session.run(""" 
       MATCH (r:Repository {name: $repo}) 
       DETACH DELETE r 
       """, repo=repo) 
