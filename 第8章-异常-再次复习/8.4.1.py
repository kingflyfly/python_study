while True:
    try:
        x = int(input("x ="))
        y = int(input("y = "))
        value = x / y
        print(value)
    except (ZeroDivisionError,ValueError) as e:
        print(e)
    else:
        break