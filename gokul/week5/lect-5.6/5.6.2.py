#  create a recursive function to return the factorial  of a given number
def fact(n):
    if (n==1):
        return 1
    else :
        return (fact(n-1))*n
print(fact(5))