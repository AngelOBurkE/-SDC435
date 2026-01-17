#Angelo Burke
#4.3 GP Neo4j integration
#Jan 17, 2026
def show_user_repos(neo_mgr): 
    user = input("Enter username: ") 
    repos = neo_mgr.get_user_repos(user) 
    print(f"\nRepositories committed to by {user}:") 
    for r in repos: 
        print("-", r)   
  
def repos_by_language(neo_mgr): 
    language = input("Enter language: ") 
    with neo_mgr.driver.session() as session: 
        result = session.run(""" 
        MATCH (r:Repository)-[:USES_LANGUAGE]->(l:Language {name: $lang}) 
        RETURN r.name 
        """, lang=language) 
        print(f"\nRepositories using {language}:") 
        for record in result: 
            print("-", record["r.name"]) 
  
def most_active_users(neo_mgr): 
    with neo_mgr.driver.session() as session: 
        result = session.run(""" 
        MATCH (u:User)-[:COMMITTED_TO]->(r) 
        RETURN u.name AS user, COUNT(r) AS commits 
        ORDER BY commits DESC 
        LIMIT 5 
        """) 
        print("\nMost Active Users:") 
        for record in result: 
            print(record["user"], "-", record["commits"]) 
