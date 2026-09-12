# create a python function that takes a list as input and returns the minimum element in the list

# create a python function that takes a list as input and returns the maximum element in the list

# call these two functions and create one list in ascending order and another list in 
# descending order by taking the list i

# eg : [1,22,32,12,42,15]

# l=list(input("l:"))
# l.sort
# def smol(l):
#     min1=l[0]
#     return min1
# smol=smol(l)
# print (smol)

# def mox (l):
#     max1=l[-1]
#     return max1 
# mox=mox(l)
# print(mox)

# a=[]
# a.append
# print gejtriogj


l=[1,4,2,5,3]

def minimum(l):
    return min(l)

def maximum(l):
    return max(l)

# ascending order

def ascending_order(l):
    op=[]
    while l:
        minimum_elem=minimum(l)
        op.append(minimum_elem)
        l.remove(minimum_elem)
    print(op)

ascending_order(l)
