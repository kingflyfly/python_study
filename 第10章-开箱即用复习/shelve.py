import shelve
s = shelve.open("test.txt")
s["x"]  = ["a","b","c"]
s["x"].append("d")
print(s["x"])