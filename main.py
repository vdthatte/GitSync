import urllib.request
import json

# https://api.github.com/repos/vdthatte/GitSync-TestRepo/git/commits/0da841c86c460941bcd22bb865fa939e9666c4d0


tree_url = ""

with urllib.request.urlopen('https://api.github.com/repos/vdthatte/GitSync-TestRepo/git/commits/0da841c86c460941bcd22bb865fa939e9666c4d0') as response:
   commit_json = json.load(response)
   sha = commit_json['sha']
   tree_url = commit_json['tree']['url']

with urllib.request.urlopen(tree_url) as tree_data:
	tree_json = json.load(tree_data)
	print(tree_json)


# STEP 1
#get the current commit object

# STEP 2
#retrieve the tree it points to

# STEP 3
#retrieve the content of the blob object that tree has for that particular file path

# STEP 4
#change the content somehow and post a new blob object with that new content, getting a blob SHA back

# STEP 5
#post a new tree object with that file path pointer replaced with your new blob SHA getting a tree SHA back

# STEP 6
#create a new commit object with the current commit SHA as the parent and the new tree SHA, getting a commit SHA back

# STEP 7
#update the reference of your branch to point to the new commit SHA

