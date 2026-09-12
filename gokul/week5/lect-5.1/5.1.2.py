# create a function named `sub` that takes three parameters as input and  returns their the minimum difference among the three
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
lis=[]
lis.extend([a,b,c])
lis.sort()
print(lis)
mindiff=1
def sub(lis):
    for i in lis :
        mindiff= lis[1]-lis[0]
        return mindiff 

print("mindiff:" , (sub(lis)))

        

# def sub (a,b,c):
    

#     # min1=abs(a-b)
#     # min2=abs(b-c)
#     # min3=abs(c-a)
#     # result=0
#     # if min1>=min2 and min2>=min3:
#     #     result=min3
#     # elif min3>=min2 and min2>=min1:
#     #     result=min1
#     # elif min2>=min1 and min1>=min3:
#     #     result=min3
#     # return result 
# sub=sub(a,b,c)
# print(sub)



# alternatives for li.append as it takes only one arg 
# lis.insert() only takes 2 elements 
# lis.extend([]) takes multiple 