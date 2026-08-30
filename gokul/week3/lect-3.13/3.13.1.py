## write a code for the below test cases

# print until you find @ in the string, using break statement
# TestCase 1
# INPUT="abcd@gmail.com"
# OUTPUT:
'''
a
b
c
d
'''
inp=str(input("enter mail"))
for c in inp:
    if c=="@":
        break
    print(c)

# for x in range (11): 
#     if (x % 3 == 0):
#         print (x)
#     else:
#         pass