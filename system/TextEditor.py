import sublime
import sublime_plugin
import json
import sys
import os
import urllib
import base64
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), "github"))

#from threading import Timer

#from . import GUI
from . import GitApi
from . import GUI
#
gui = None
git = None

key_added = False


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
	key_added = True



class CommitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global key_added
		global git
		global branch_names
		if(not key_added):
			setup()
			key_added = True
		#self.view.insert(edit, 0, "Commited Work\n")
		path = urllib.parse.unquote(self.view.file_name()) 
		content = self.view.substr(sublime.Region(0, self.view.size()))
		git.commit(path, content)
		

class BranchCommand(sublime_plugin.TextCommand):
	
	def selectBranch(self, val):
		global key_added
		global git
		if(not key_added):
			setup()
			key_added = True
		if(val == 0):
			print("create new branch")
		else:
			os.system('git checkout '+branch_names[val])


	def run(self, edit):
		global key_added
		global git
		global branch_names
		if(not key_added):
			setup()
			key_added = True
		#self.view.insert(edit, 0, "Created a New Branch\n")
		path = urllib.parse.unquote(self.view.file_name())
		branch_names = git.branch(path)
		
		self.view.window().show_quick_panel(branch_names,self.selectBranch, 0, 0, 0)



class MergeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global key_added
		global git
		if(not key_added):
			setup()
			key_added = True
		path = urllib.parse.unquote(self.view.file_name())
		
		git.merge(path)


class InfoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global key_added
		global git
		if(not key_added):
			setup()
			key_added = True
		self.view.show_popup("Hey, what's up?", max_width=500)
		#self.view.window().show_quick_panel(["Master","New Branch"],"on_done",0,0,0)
		#self.view.window().show_input_panel("caption", "initial_text", "on_done", "on_change", "on_cancel")
		#self.view.insert(edit, 0, "Opening GUI.....\n")

def setup():
	
	global git
	global gui

	addKeyBindings()
	gui = GUI.GUI(sublime_plugin.WindowCommand(sublime.active_window()))
	git = None
	gui.login()
	
	#sublime.active_window().run_command('plug')
	usr, password = ['usr', 'pss'] #Change login info here!!!
	git = GitApi.GitApi(usr, password)

	autoSave(t)



