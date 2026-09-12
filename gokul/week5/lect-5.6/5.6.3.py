# compute the compound interest by taking in p,n as arguments and interest rate = 10%
# p-> principal amount, n-> number of years


def comp(p,n):
    if (n == 1):
        return p*(1.1)
    else:
        return comp(p,n-1)*1.1

# print(sum(10))
print(comp(2000,3))