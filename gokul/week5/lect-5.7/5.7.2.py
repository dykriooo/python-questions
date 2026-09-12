# what will be the output

def add1(a,b=10,c=20):
    return a+b-c

def add2(c,b,a):
    return a+b-c

# ip : add1(1,2) -17
# ip : add1(1) 9
# ip : add1(a=1,2,3) syntax error 

# add1=add1(a=1,2,3) 
# add2=add2(c,b,a)
print(add1)