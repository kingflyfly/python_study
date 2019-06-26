def inc(x):return  x + 1
foo = 2
foo = inc(foo)
print(foo)

def inc1(x):x[0] = x[0] + 1
foo = [4]
inc1(foo)
print(foo)
