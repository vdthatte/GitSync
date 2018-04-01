from github import Github

g = Github("c514d06de71b221a8ebb88916675b2e13a059600")

print(g.get_user().avatar_url)
