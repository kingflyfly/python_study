#import this
#f = open("somefile.txt")
#print(f)
#f = open("D:\\passwd.txt","w")
#f.write("hello,world")
#f.close()

#try:
#    f = open(r"D:\passwd.txt","a")
#    f.writelines("yanzhe\nyanzhe")
#finally:
#    f.close()
#d = open(r"D:\passwd.txt")
#print(d.readlines())
f = open(r"D:\passwd.txt")
print(f.read())
f = open(r"D:\passwd.txt")
for i in range(1,3):
#   print(str(i) + ": " + f.readline())
   print(str(i) + ": " + f.readline(),end="")
f = open(r"D:\passwd.txt")
print(f.read())
def process(string):
   print("process:",string)
with open(r"D:\passwd.txt") as d:
   char = d.read(1)
   while char:
      process(char)
      char = d.read(1)
