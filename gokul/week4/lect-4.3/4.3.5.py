# predict the output

l=[1,[2,3],[[4,5],[6,7],[[8,9],10,11],[12]],13]
print(len(l)) 
# 4
# print(len(l[0]))type error
print(len(l[1]))
# 2
print(len(l[2]))
# 4
print(len(l[2][2]))

# print(len(l[-1]))
# syntax error (),type error 13 is an integer
# print(len(l[-2])) 
# syntax error()
