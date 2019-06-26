def process(string):
   print("process:",string)
with open(r"D:\passwd.txt") as d:
   char = d.read(1)
   while char:
      process(char)
      char = d.read(1)
