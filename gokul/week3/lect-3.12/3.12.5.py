# ![alt text](image-3.png)
word=input("enter a word ")
maxlen=0
while (word != '-1'):
    count=0
    for letter in word:
        count=count+1
    if(count > maxlen):
        maxlen=count
    word=input("enter a word:")
print("longest word:" %maxlen)