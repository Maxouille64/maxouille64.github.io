import urllib.request, jsongithub_link = "https://github_username.github.io/json_file.json"with urllib.request.urlopen(github_link) as url: 
   json_data = json.loads(url.read().decode())print(json_data)
