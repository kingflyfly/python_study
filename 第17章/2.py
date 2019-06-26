import requests
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
#print("status code:",r.status_code)
t = r.json()
print(t)