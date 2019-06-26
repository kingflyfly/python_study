import copy
print(dir(copy))
print([n for n in dir(copy) if not n.startswith("_")])
print(copy.__all__)
print(help(copy))
print(copy.copy(__doc__))


print(range.__doc__)
print(copy.__file__)