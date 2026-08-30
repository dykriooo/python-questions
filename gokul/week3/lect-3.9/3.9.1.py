# write a code to get the output as below using for loop
# note: you can use two for loops if needed
'''
OUTPUT: '1 2 3 4 5 6 7 8 9'
OUTPUT: '1,2,3,4,5,6,7,8,9,'

'''
out1=""
for i in range (1,10):
    out1 += str(i) + " "
print(out1)

out2=""
for i in range (1,10):
    out2 += str(i) + ","
print(out2)