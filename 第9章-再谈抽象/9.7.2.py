def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(nested):
    except TypeError:
        yield nested

list(flatten([[1,2],2]))