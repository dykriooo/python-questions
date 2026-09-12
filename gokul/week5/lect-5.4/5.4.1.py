# create a function that takes two list as input and return their dot products as output

'''
sample test case
l1=[1,2,3]
l2=[4,5,6]
dot_product(l1,l2)

# ans : 32
'''

# # l3=[4,6,7]
# def dotprod (l1,l2):
#     for i in l1:
#         for j in l2:
#             if [i]==[j]:
#                 dot=i*j
#                 return dot 
# dotprod=dotprod(l1,l2)
# print(dotprod)
            
# print lgnvelwjg

# def mat (dim):
#     c=[]
#     for i in range (dim):
#         c.append([])
#     for i in range (dim):
#         for j in range (dim):
#             c[i].append(0)
#     return c
# print(mat(3))
# l1=[1,2,3]
# l2=[4,5,6]
# def dotprod (l1,l2):
#     dim=len(l1)
#     ans=0 
#     for i in range (dim):
#         ans=ans + (l1[i]*l2[i])
#     return ans 

# print(dotprod(l1,l2))

l1 = [1, 2, 3]
l2 = [4, 5, 6]

def dotprod(l1, l2):
    dim = len(l1)
    ans = 0

    for i in range(dim):
        ans = ans + (l1[i] * l2[i])

    return ans

print(dotprod(l1, l2)) 