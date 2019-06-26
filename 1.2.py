while True:
    try:
        a = int(input("first:"))
        b = int(input("second:"))
        print(a / b)
        break
    except ZeroDivisionError:
        b = int(input("second:"))
        print(a / b)