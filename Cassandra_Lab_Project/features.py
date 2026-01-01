#Angelo Burke
#3.3 Project
#January 1, 2026
from collections import Counter 
  
# Feature 1: Trending repositories (most commits) 
def trending_repos(commits): 
    counter = Counter() 
    for c in commits: 
        counter[c.repo_name] += 1   
    print("\nTrending Repositories:") 
    for repo, count in counter.most_common(5): 
        print(repo, "-", count, "commits")                                                                                                                                                                                                                                                                                          
  
# Feature 2: Most common words in commit messages 
def common_commit_words(commits): 
    words = {} 
    for c in commits: 
        if c.message: 
            for word in c.message.lower().split(): 
                words[word] = words.get(word, 0) + 1 
    print("\nMost Common Commit Words:") 
    for w in sorted(words, key=words.get, reverse=True)[:5]: 
        print(w, "-", words[w]) 

# Feature 3: Display commits by a specific author 
def commits_by_author(commits, author_name): 
    print(f"\nCommits by {author_name}:") 
    for c in commits: 
        if c.author == author_name: 
            print("-", c.message) 
