# ![alt text](image-1.png)
empid = input ("enter:")
while(empid != '-1'):
    trade=int(input("enter the trade amount :"))
    profitloss=0
    while(trade != 0):
        profitloss=profitloss + trade 
        trade = int (input("enter a number :"))
    print(empid , profitloss)

