import sublime
import sublime_plugin
import json
import sys
import os
import urllib
import base64
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), "github"))


from . import GUI
from . import GitApi


#
gui = None
git = None


# https://api.github.com/repos/vdthatte/GitSync-TestRepo/git/trees/{latest commit sha}
# view.run_command('commit')

#Keys for Commands
#control+shift+s => Commit
#control+shift+b => New Branch
#control+shift+m => Merge Branch
#control+shift+u => Open UI

branch_names = ["Create New Branch"]

def addKeyBindings():
	keys = ['{ "keys": ["control+shift+s"], "command": "commit" },', \
		'{ "keys": ["control+shift+b"], "command": "branch" },', \
		'{ "keys": ["control+shift+m"], "command": "merge" },', \
		'{ "keys": ["control+shift+u"], "command": "info" },'
		]

	path = "/Users/shivamswarnkar/Library/Application Support/Sublime Text 3/Packages/User/Default (OSX).sublime-keymap"
	fh = open(path, 'r')
	curr = [i.strip() for i in fh.readlines()]
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
		git.commit()
		
		

class BranchCommand(sublime_plugin.TextCommand):
	
	def selectBranch(self, val):
		if(val == 0):
			print("create new branch")
		else:
			print(branch_names[val])


	def run(self, edit):
		#self.view.insert(edit, 0, "Created a New Branch\n")
		branch_names = git.branch()
		
		self.view.window().show_quick_panel(branch_names,self.selectBranch, 0, 0, 0)

class MergeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		git.merge()


class InfoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.show_popup("Hey, what's up?", max_width=500)
		#self.view.window().show_quick_panel(["Master","New Branch"],"on_done",0,0,0)
		#self.view.window().show_input_panel("caption", "initial_text", "on_done", "on_change", "on_cancel")
		#self.view.insert(edit, 0, "Opening GUI.....\n")

def main():
	
	addKeyBindings()
	gui = GUI()
	
	
	while not git:
		try:
			usr,password = gui.login() 
			git = GitApi(user, password)
		except:
			print("WRONG USERNAME OR PASSWORD, Try Again")




main()

