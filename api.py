from github import Github

g = Github("c514d06de71b221a8ebb88916675b2e13a059600")

repo = g.get_user().get_repo('GitSync-TestRepo')

content = 'c2FzZGFzZADDDDDdasdas==\n'

commit = repo.get_commits()[0]
tree = repo.get_git_tree(commit.sha)

for element in tree.tree:
	if(element.path == 'hello.txt'):
		print(element.sha)