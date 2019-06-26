def process(string):
    print("process:",string)
with open(r"d:\passwd.txt") as d:
    for char in d.read():
        process(char)
with open(r"D:\passwd.txt") as f:
    for line in f.readlines():
        process(line)