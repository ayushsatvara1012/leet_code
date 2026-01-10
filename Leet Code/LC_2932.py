from itertools import combinations, combinations_with_replacement
import operator

def maxXOR(num):
    max_xor = 0
    for i,j in combinations_with_replacement(num,2):
        if abs(i-j) <= min(i,j):
            max_xor = max(max_xor , i^j)
    return max_xor

maxXOR([1,2,3,4,5])