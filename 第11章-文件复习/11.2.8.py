c = "print('ok')"
exec(c)
import os
print(os.name,os.getcwd(),os.getenv("PATH"))
print(os.listdir())
import time
print(time.time())
print(time.ctime())
print(time.sleep(2))