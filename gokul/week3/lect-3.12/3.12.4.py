# ![alt text](image-2.png)
days=int(input ("days:"))
for i in range (1,days+1):
    total=0
    rainfall=int(input("rain:"))
    while (rainfall != -1):
        total=total+rainfall
        rainfall=int(input("eneter the rainfall"))
    print("total rainfall for (0) in (1).format(i,total) ")

