import sublime
import sublime_plugin

#Save this file at 
#/Users/UserName/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/

#Keys for Commands
#control+shift+s => Commit
#control+shift+b => New Branch
#control+shift+m => Merge Branch
#control+shift+u => Open UI


#Key Bindings 
'''[
	{ "keys": ["control+shift+s"], "command": "commit" },
	{ "keys": ["control+shift+b"], "command": "branch" },
	{ "keys": ["control+shift+m"], "command": "merge" },
	{ "keys": ["control+shift+u"], "command": "info" }
]'''

class CommitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Commited Work\n")
class BranchCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Created a New Branch\n")

class MergeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Merged the current branch with Master branch\n")

class InfoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Opening GUI.....\n")
