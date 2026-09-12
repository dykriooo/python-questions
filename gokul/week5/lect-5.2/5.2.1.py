'''
create three functions that take a list as input 
1) to return the first element of the list
2) to return the last element of the list
3) to return the sum of values returned from the above two functions 
'''

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
lis=[]
lis.extend([a,b,c])
lis.sort()
def lista (lis) :
    index0=lis[0]
    return index0

print(lista(lis))

def listb (lis) :
    index1=lis[1]
    return index1

print(listb(lis))

def listc (lis) :
    return lista(lis)+listb(lis)
    
# listc=listc(lis)
# print(listc)
print(listc(lis))
# print bfwrlfbk