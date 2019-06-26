import shelve
s = shelve.open("test.data")
#s["x"] = ["a","b","c"]
s["x"] = ["a","b","c"]
temp = s
temp.append("d")
s = temp
print(s)