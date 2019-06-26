fibs = [0,1]
num = int(input("How many Fibonacci numbers do you want? "))
for var in range(num-2):
    print("第",var,"行",":",fibs[-1],fibs[-2])
    fibs.append(fibs[-1] + fibs[-2])
print(fibs)
