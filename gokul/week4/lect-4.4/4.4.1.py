## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
# after sorting, print the smallest, second smallest, largest and second largest number in the list
import random
l=[]
for i in range (10):
    l.append(random.randint(1,1000) )
print(l)
l.sort()
print(l)
print(l[1],l[2],l[-1],l[-2])