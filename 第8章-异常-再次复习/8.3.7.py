x = None
try:
    x = 1/0
finally:
    print("cleaning up")
    del x