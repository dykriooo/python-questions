# predict the output

l=[]
l.append(1)
l.append(2)
l.append(3)
print(l)
# [1,2,3]
x=[]
print(len(x))
# 0
x.append(l)
print(x)
# [[1,2,3]]
print(len(x),"len(x)")
# 1
print(len(x[0]),"len(x[0])")
# 1,2,3
m=[4,5,6]
x.append(m)
print(x) 
# [[1, 2, 3], [4, 5, 6]]
t=[]
t.append(x)
t.append([100,200,300])
print(t)

# [[[1, 2, 3], [4, 5, 6]], [100, 200, 300]]
print(t[0])
# [[1, 2, 3], [4, 5, 6]]
print(t[1])
# [100, 200, 300]