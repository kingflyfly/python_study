nested = [[1,2],[3,4],[5]]
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
#flatten(nested)
for num in flatten(nested):
    print(num)
g = ((i + 2) ** 2 for i in range(2,27))
print(next(g))