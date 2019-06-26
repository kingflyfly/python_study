num = int(input("How many numbers do you want?"))
def fibs(num):
    fibs = [0,1]
    for var in range(num-2):
        #print("第",var,"行",":",fibs[-1],fibs[-2])
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

print(fibs(num))
