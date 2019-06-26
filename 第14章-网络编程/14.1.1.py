print("hello python,I love you!")
from urllib.request import urlopen
webpage = urlopen('http://www.baidu.com')
print(webpage.read().decode('utf-8'))
