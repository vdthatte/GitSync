from github import Github

g = Github("c514d06de71b221a8ebb88916675b2e13a059600")

repo = g.get_user().get_repo('GitSync-TestRepo')

content = 'c2FzZGFzZADDDDDdasdas==\n'

file_sha = '4407df2d7f3881db3f5db1018b2b916d55b06d14'

def get_branches(repo):
	branches = []
	for branch in repo.get_branches():
		branches.append(branch)
	return branches

def newFile(repo, file_name, content):
	print(repo.create_file('/new.txt', "test commit 1", content))

def updateFile(repo, file_name, content, file_sha):
	print(repo.update_file('/' + file_name, "update", content, file_sha))

