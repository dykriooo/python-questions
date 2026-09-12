# write a piece of code to  find the dot product.

x=[1,7,3,4]
y=[8,6,3,2]

for i in x:
    for j in y:
        if [i]==[j]:
            i*=j
            i+=i
            print(i)
