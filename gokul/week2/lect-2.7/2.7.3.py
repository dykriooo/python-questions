# predict the output


alpha="abcdefghijklmnopqrstuvwxyz"
i=24

print(alpha[i+1]) #z
#print(alpha[i+2]) #out of range
#rint(alpha[i+2]%26) #out of range 
print(alpha[(i+2)%26]) 
