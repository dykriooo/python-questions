#  create a function that returns the average of the elements present in the list
# numbers=list(input("l:"))
lis=[]
a=int(input("a:"))
b=int(input("a:"))
c=int(input("a:"))
lis.extend([a,b,c])
def average(lis):
    total = 0

    for i in lis:
        total = total + i

    avg = total / len(lis)

    return avg

average=average(lis)

print(average)
# print bewgfilw