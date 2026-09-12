## write a python code to print the minimum element of the list, using for loop

l=[1,44,22,11,23,36,49,28,31,8,54,54]
last=l[0]
for i in l:
    if l < last :
        last = i 
print(last)
        