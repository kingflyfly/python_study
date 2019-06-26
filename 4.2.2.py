class Users(object):
    online_count = 0
    def __init__(self):
        Users.online_count += 1
    def __del__(self):
        Users.online_count -= 1
a = Users()
a.online_count += 1
#print(Users.b)
print(Users.online_count)
#print(b)