
import sublime_plugin
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "github"))

from . import github
from github import Github

g = Github("c514d06de71b221a8ebb88916675b2e13a059600")

repo = g.get_user().get_repo('GitSync-TestRepo')

content = 'c2FzZGFzZADDDDDdasdas==\n'
# https://api.github.com/repos/vdthatte/GitSync-TestRepo/git/trees/{latest commit sha}
# view.run_command('commit')

#Keys for Commands
#control+shift+s => Commit
#control+shift+b => New Branch
#control+shift+m => Merge Branch
#control+shift+u => Open UI

def addKeyBindings():
	keys = ['{ "keys": ["control+shift+s"], "command": "commit" },', \
		'{ "keys": ["control+shift+b"], "command": "branch" },', \
		'{ "keys": ["control+shift+m"], "command": "merge" },', \
		'{ "keys": ["control+shift+u"], "command": "info" },'
		]

	path = "/Users/shivamswarnkar/Library/Application Support/Sublime Text 3/Packages/User/Default (OSX).sublime-keymap"
	fh = open(path, 'r')
	curr = [i.strip() for i in fh.readlines()]
	print(curr)
	for i in keys:
		if(i not in curr):
			curr.insert(len(curr)-1, i)
	fh.close()

	fh = open(path, 'w')
	for k in curr:
		fh.write(k+"\n")
	fh.close()


class CommitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Commited Work\n")
		commit = repo.get_commits()[0]
		tree = repo.get_git_tree(commit.sha)

		for element in tree.tree:
			if(element.path == 'hello.txt'):
				print(repo.update_file('/new.txt', "update", content, element.sha))




class BranchCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Created a New Branch\n")

class MergeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Merged the current branch with Master branch\n")

class InfoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Opening GUI.....\n")

def main():
	
	addKeyBindings()


