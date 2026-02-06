def two_sum(nums,target):
    look_up = {}

    for index,val in enumerate(nums):
        complement = target - val
        if complement in look_up:
            return [look_up[complement],index]
        look_up[val]=index

print(two_sum([2,7,11,15],9))