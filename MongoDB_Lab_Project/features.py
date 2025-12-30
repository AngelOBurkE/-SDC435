#Angelo Burke
#2.3 GP MongoDB Integration
#December 29, 2025
from collections import Counter 

# Feature 1: Longest & shortest commit messages 
def message_length_survey(mongo_mgr): 
    commits = mongo_mgr.commits.find() 
    messages = [c["message"] for c in commits] 

    if not messages: 
        print("No commit data found.") 
        return 

    print("Longest message:", max(messages, key=len)) 
    print("Shortest message:", min(messages, key=len))
    
# Feature 2: Watch count distribution 
def watch_distribution(mongo_mgr): 
    commits = mongo_mgr.commits.find() 
    counts = [c.get("watch_count", 0) for c in commits] 
    print("Watch count distribution:", counts) 

# Feature 3: Most common words in commit messages 
def popular_commit_words(mongo_mgr): 
    commits = mongo_mgr.commits.find() 
    words = [] 
    for c in commits: 
        words.extend(c["message"].lower().split()) 
    counter = Counter(words) 
    print("Most common words:", counter.most_common(5)) 
