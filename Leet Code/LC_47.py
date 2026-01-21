def unique_permutations(nums):
    if len(nums)<2:
        return [nums]
    nums.sort()
    result = []
    for i in range(len(nums)):
        curr_ele = nums[i]
        remaining_ele = nums[:i]+nums[i+1:]
        if i>0 and nums[i]==nums[i-1]:
            continue
        for p in unique_permutations(remaining_ele):
            result.append([curr_ele]+p)

    return result
print(unique_permutations([1,1,2]))