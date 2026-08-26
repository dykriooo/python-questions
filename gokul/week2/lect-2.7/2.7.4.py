
# write a python script for the below test case,
# Note the input will be of 5 characters long,

# OUTPUT : 'hplvm'
# testcase 1
alpha ="abcdefghijklmnopqrstuvwxyz"
a: 'gokul'



# Loop through each character in the string
text = "abcde"
result = ""

for ch in text:
    result += chr(ord(ch) + 1)

print(result)
  # Output: bcdef


# testcase 2
'''
INPUT: 'abcde'
OUTPUT: 'bcdef'
'''

# solution:
alpha ="abcdefghijklmnopqrstuvwxyz"
ip=input()
op=""
for i in ip :
  op+=alpha[alpha.index(i)%26]
  print (op)