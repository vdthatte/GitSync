import urllib.request
import urllib.parse
import json

# https://api.github.com/repos/vdthatte/GitSync-TestRepo/git/commits/0da841c86c460941bcd22bb865fa939e9666c4d0

# curl -X POST -H "Authorization: token c896ec4c24f3371dd9a71c06b95644a0116f3dda" https://api.github.com/repos/vdthatte/GitSync-TestRepo/git/commits -d '{"message": "my commit message","author": {"name": "Scott Chacon","email": "vd_thatte@yahoo.com","date": "2008-07-09T16:13:30+12:00"},"parents": ["b40efdaff52e4197af175b49b2922e82b6b6f846"],"tree": "aff8f0a483ce3dbd1ed916fde223717664e91e9e"'
tree_url = ""


data = urllib.parse.urlencode({

  "message": "my commit message",
  "author": {
    "name": "Scott Chacon",
    "email": "schacon@gmail.com",
    "date": "2008-07-09T16:13:30+12:00"
  },
  "parents": [
    "b40efdaff52e4197af175b49b2922e82b6b6f846"
  ],
  "tree": "aff8f0a483ce3dbd1ed916fde223717664e91e9e",

}).encode("utf-8")

headers = {
	"Authorization": 'c896ec4c24f3371dd9a71c06b95644a0116f3dda'
}

req = urllib.request.Request("https://api.github.com/repos/vdthatte/GitSync-TestRepo/git/commits", data, headers)
response = urllib.request.urlopen(req)

print(response.read())
