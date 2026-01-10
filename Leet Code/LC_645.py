def setMismatch(nums):
    n = len(nums)
    actual_sum = sum(nums)
    actual_set = set(nums)

    dup = actual_sum - sum(actual_set)
    missing = n * (n+1)//2 - sum(actual_set)

    return [dup,missing]
print(setMismatch([2,2]))
print(setMismatch([1,2,2,4]))
print(setMismatch([1,1]))