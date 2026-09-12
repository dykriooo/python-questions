# create a function discount that takes two arguments cost and d 'discount percentage' as input
# ,and it should return the cost after reducing the discounted price from the original price

# Test cases
# ip : discount(100,50)
# op : 50

# ip : discount(200,20)
# op: 160


discount_percentage=int(input("discount percentage:"))
cost=int(input("cost:"))
def discount (cost,discount_percentage):
    disc=cost*discount_percentage/100
    result=cost-disc
    return result
# discount=discount(cost,discount_percentage)
# print(discount)
print("discount:" , discount(cost,discount_percentage))

# def discount (cost,d):
#     ans=cost-(cost*(d/100)) 
#     print(ans)
# discount(100,8)