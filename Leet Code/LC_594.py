#Longest Harmonious Subsequence
from collections import Counter

def findLHS(nums):
    """Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences."""
    count = Counter(nums)
    length = 0
    for num in count:
        if num + 1 in count:
            l = count[num] + count[num + 1]
            length = max(length, l)
    return length
