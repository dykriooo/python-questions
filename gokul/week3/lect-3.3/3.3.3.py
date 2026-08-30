# find the factorial of a number using while loop, take number n as input
n=int (input ())
fact=1

while n>=0:
    fact*=n
    n-=1
print(fact) 
