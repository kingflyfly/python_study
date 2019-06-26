
def jisuan():
    try:
        x = int(input("first number:"))
        y = int(input("second number:"))
        print(x / y)
    except ValueError:
        print("That wasn't a number, was it?")
    except ZeroDivisionError:
        print("The second number can't be zero!")
jisuan()