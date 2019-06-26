#from time import *
#from random import *
#print(random())
#print(uniform(0,100))
#print(randrange(1,100,2))
#list = [2,3,4,45654,78768]
#print(choice(list))
#date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
#time1 = mktime(date1)
#print(time1)
#date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
#time2 = mktime(date2)
#print(time2)
#random_time = uniform(time1, time2)
#print(random_time)
#print(asctime(localtime(random_time)))
print(list(range(2)))

from random import randrange
print(randrange(10))
num = int(input("How many dice?"))
sides = int(input("How many sides per die?"))
sum = 0
for i in range(num):
    #sum +=randrange(sides) + 1
    sum = sum + randrange(sides) +1
print(sum)
