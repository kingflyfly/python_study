try:
    1 / 3
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("cleaning up")