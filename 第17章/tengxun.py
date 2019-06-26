import requests
url = "https://graph.qq.com/user/get_user_info"
r = requests.get(url)
print(r.status_code)
t = r.json()
print(t)
for key,value in t.items():
       print(key,':',value)