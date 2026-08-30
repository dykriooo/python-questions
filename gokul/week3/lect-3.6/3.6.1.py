# take a number as input and find the sum of numbers from 1 to that number
# num=int (input ())
# total=0
# for i in range (1,num+1):
#     total +=i
# print(total)

num = int(input("Enter a number: "))
total_sum = (num * (num + 1)) // 2
print(f"The sum is: {total_sum}")

