def process(string):
    print("process:",string)
with open(r"D:\passwd.txt") as d:
    while True:
        line = d.readline()
        if not line: break
        process(line)
