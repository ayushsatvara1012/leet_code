def dominantIndex(nums):
    new_nums = sorted(nums)
    if new_nums[-2]*2 <= new_nums[-1]:
        return nums.index(new_nums[-1])
    return -1
print(dominantIndex([1,2,6,5,4,12]))