from github import Github

g = Github("c514d06de71b221a8ebb88916675b2e13a059600")

repo = g.get_user().get_repo('GitSync-TestRepo')

content = 'c2FzZGFzZADDDDD==\n'

print(repo.create_file('/new.txt', "test commit 1", content))



