'''
print(set(range(10)))
print(type({}))
print({1,2,3,4,5,5,6,6,6,7,8})
print({'fee', 'fie', 'foe'})
a = {1,2,3}
b = {4,5,6}
print(a.union(b))
print(a|b)
c = a & b
print(c)
print(c.issubset(a))
print(a - b )

from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
print(data)
heap = []
for n in data:
    heappush(heap,n)
print(heap)
heappush(heap,0.5)
print(heap)
print(heappop(heap))
print(heap)'''
