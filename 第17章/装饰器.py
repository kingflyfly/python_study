def test(func):
    def test1():
        print(3)
        func()
    return test1

@test
def test2():
    print(2)

test2()