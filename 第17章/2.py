import requests
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
t = r.json()
print(t)