def addDigit(n):
    if n==0:
        return 0
    return 1+(n-1)%9
print(addDigit(38))