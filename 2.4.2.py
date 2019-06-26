t = (1,2,34,"df")
print(t)
print(t[0]);print(t[1]);print(len(t))
for var in range(len(t)):
    print(t[var])
print(t)
for index,value in enumerate(t):
    print("第%d个元素的值为 %s"%(index,value))
