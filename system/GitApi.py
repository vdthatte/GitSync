
import json
import sys
import os
import urllib
import base64
import datetime
from .GitApi import GitApi
from .GUI import GUI


class GitApi:
	def __init__(self, usr,pas):
		#Login into the git
		__self.username = username
		self.file_name = ""
		self.branch_names = ["Create New Branch"]

		#self.g = Github("c514d06de71b221a8ebb88916675b2e13a059600")
		self.g = Github(self.username, pas)

		#test if Github login was succesful 
		g.get_user().get_repos()


	def commit(self):
		path = urllib.parse.unquote(self.file_name)
		dirPath = os.path.dirname(path)
		repoName = os.path.basename(dirPath)
		repo = g.get_user().get_repo(repoName)
		commit = repo.get_commits()[0]
		tree = repo.get_git_tree(commit.sha)
		filename = os.path.basename(path)
		print(datetime.date.year)
		commit_message = "update: "
		print(base64.b64decode(repo.get_file_contents(filename).content))
		for element in tree.tree:
			if(element.path == filename):
				print(repo.update_file('/' + filename, commit_message, element.sha))

	def branch(self):
		#self.view.insert(edit, 0, "Created a New Branch\n")
		path = urllib.parse.unquote(self.file_name)
		dirPath = os.path.dirname(path)
		repoName = os.path.basename(dirPath)
		repo = g.get_user().get_repo(repoName)
		branches = repo.get_branches()
		print(repo.branches_url)
		for branch in branches:
			self.branch_names.append(branch.name)
		return self.branch_names


	def merge(self):
		path = urllib.parse.unquote(self.file_name)
		dirPath = os.path.dirname(path)
		repoName = os.path.basename(dirPath)
		repo = g.get_user().get_repo(repoName)
		base = repo.master_branch
		head = repo.default_branch
		print(head)
		print(base)
		print(repo.merge(base, head))





