def thirdMaxNumber(nums):
    if len(nums) < 3:
        return max(nums)

    sort_nums = sorted(dict.fromkeys(nums).keys(),reverse=True)
    return sort_nums[2]

print(thirdMaxNumber([1,2,1, 2,3,4]))
