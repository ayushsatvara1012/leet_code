def isPowerOfTwo(n):
    if n<=0:
        return False
    while n%2 == 0:
        n = n//2
    return n==1

#  Bit manipulation
    #return n>0 and (n & (n-1) == 0)
print(isPowerOfTwo(8))