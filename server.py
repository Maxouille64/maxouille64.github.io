import urllib.request, jsongithub_link = "https://github.com/Maxouille64/database/blob/main/teams.json" with urllib.request.urlopen(github_link) as url: 
   json_data = json.loads(url.read().decode())print(json_data)
