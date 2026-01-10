def defuseBomb(code, k):
    """You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k."""
    '''
    k>0 : replace with the next sum() of next k elements
    i=0 and i+1 i+2 i+3
    0+1 % 4 = 1
    0+2 % 4 = 2
    '''
    n = len(code)
    result = [0]*n
    if k==0:
        return result

    if k>0:
        print(result)
        for i in range(n):
            total = 0
            for j in range(1,k+1):
                total += code[(i+j)%n]
                result[i] = total
        print(result)

    if k<0:
        for i in range(n):
            total = 0
            for j in range(1,abs(k)+1):
                total += code[(i-j)%n]
                result[i] = total
        print(result)
defuseBomb([2,4,9,3],-2)