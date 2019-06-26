storge = {}
storge['first'] = {}
storge['middle'] = {}
storge['third'] = {}
print (storge)
me = 'Magnus Lie Hetland'
storge['first']['Magnus'] = [me]
storge['middle']['Lie'] = [me]
storge['third']['Hetland'] = [me]
print (storge['middle']['Lie'] )
print (storge)
my_sister = 'Anne Lie Hetland'
storge['first'].setdefault('Anne', []).append(my_sister)
print(storge['first']['Anne'])
storge['middle'].setdefault('Lie', []).append(my_sister)
storge['third'].setdefault('Hetland', []).append(my_sister)
print (storge['first']['Anne'])
print (storge)

