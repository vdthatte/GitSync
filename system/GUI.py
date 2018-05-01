class GUI:
	'''
	This class opens a new input panel to take username and password.

	Attributes:
		window_obj : type: sublime_plugiin.WindowCommand
		username   : type: str
		password   : type: str
	Note : for normal use, initiate class with sublime_plugin.WindowCommand(sublime.active_window())
	'''
	def __init__(self, window):
		self.window_obj = window
		self.username = ""
		self.password = ""

	def login(self):
		'''starts an input_panel to username and password'''
		self.window_obj.window.show_input_panel( "User Name", "", self.inputUsername, None, None)
		
		print(self.username, self.password)
		return self.username, self.password


	def inputUsername(self, val):
		'''saves username, starts an input pannel to get password'''
		self.username = val
		self.window_obj.window.show_input_panel("Password", "", self.inputPassword, None, None)

	def inputPassword(self, val):
		'''saves password'''
		self.password = val



		

		
		