
import json
import sys
import os
import urllib
import base64
import datetime

#from .GitApi import GitApi
#from .GUI import GUI

from . import github
from github import Github


class GitApi:
	def __init__(self, usr,pas):
		#Login into the git
		
		self.branch_names = ["Create New Branch"]

		#self.g = Github("c514d06de71b221a8ebb88916675b2e13a059600")
		self.g = Github(usr, pas)

		#test if Github login was succesful 
		self.g.get_user().get_repos()


	def commit(self, path, content):
		dirPath = os.path.dirname(path)
		repoName = os.path.basename(dirPath)
		repo = self.g.get_user().get_repo(repoName)
		commit = repo.get_commits()[0]
		tree = repo.get_git_tree(commit.sha)
		filename = os.path.basename(path)
		print(datetime.date.year)
		commit_message = "update: "
		print(base64.b64decode(repo.get_file_contents(filename).content))
		for element in tree.tree:
			if(element.path == filename):
				print(repo.update_file('/' + filename, commit_message, content, element.sha))

	def branch(self, path):
		#self.view.insert(edit, 0, "Created a New Branch\n")
		dirPath = os.path.dirname(path)
		repoName = os.path.basename(dirPath)
		repo = self.g.get_user().get_repo(repoName)
		branches = repo.get_branches()
		print(repo.branches_url)
		branch_names = ["Create New Branch"]
		for branch in branches:
			branch_names.append(branch.name)
		return branch_names


	def merge(self, path):
		dirPath = os.path.dirname(path)
		repoName = os.path.basename(dirPath)
		repo = self.g.get_user().get_repo(repoName)
		base = 'master'
		head = self.curr_branch(dirPath)
		print('head', head)
		print('base', base)
		print(repo.merge(base, head))


	def curr_branch(self, path):
		plug_path = os.popen('pwd').read().strip()
		os.chdir(path)
		br = os.popen("git branch | grep \* | cut -d ' ' -f2").read().strip()
		os.chdir(plug_path)
		return br







