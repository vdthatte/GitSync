from github import Github

g = Github("c514d06de71b221a8ebb88916675b2e13a059600")

repo = g.get_user().get_repo('GitSync-TestRepo')

content = 'c2FzZGFzZADDDDDdasdas==\n'

#print(repo.create_file('/new.txt', "test commit 1", content))

print(repo.update_file('/hello.txt', "update", content, '4407df2d7f3881db3f5db1018b2b916d55b06d14'))
