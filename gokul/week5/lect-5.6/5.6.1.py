#   create a recursive function to return the sum  numbers from 1 to n, take  n as an argument

n=10
ans=0
for i in range (n):
    print (i+1)
    ans = ans +(i+1)

print(ans)

# def sum(n):
#     ans = 0
#     for i in range (n):
#         ans = ans + (i+1)
#     return ans
# print(sum(10))

# recurssion in python 

# def sum(n):
#     if (n==1):
#         return 1 
#     else :
#         return n + sum(n-1)
# #python lets you call the same function within the function 
# print(sum(10))



