def hello_1(greeting, name):
    print ('{}, {}!'.format(greeting, name))

def hello_2(name, greeting):
    print ('{}, {}!'.format(name, greeting))

def hello_3(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))
hello_1('Hello', 'world')

hello_2('Hello', 'world')

hello_3("hello","shanshan")

hello_3(name="gaige")

def hello_4(name, greeting='Hello', punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))

hello_4("gaige")
def print_c(**par):
    print (par)
print_c(x=1,y=2)