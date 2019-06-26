try:
    x = int(input("x="))
    y = int(input("y="))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")