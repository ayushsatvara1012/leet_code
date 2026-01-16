def four_sum(nums, target):
    """Given an array nums of n integers, return an array of all the unique quadruplets     [nums[a], nums[b], nums[c], nums[d]] such that:
        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target"""

    # -------------------------------------------------------------------------
    # CURRENTLY INCOMPLETE
    # -------------------------------------------------------------------------


    nums.sort()
    n = len(nums)
    seen = set()
    result = []
    for i in range(n-3):
        left = i + 1
        right = n - 1
        if i>0 and nums[i]==nums[i-1]:
            continue

        while left < right:
            # if [nums[i],nums[left],nums[left+1],nums[right]] in seen:
            #     continue
            target_sum = nums[i] + nums[left] + nums[left + 1] + nums[right]
            if target_sum < target:
                left += 1
            elif target_sum > target:
                right -= 1
            else:
                result.append([nums[i],nums[left],nums[left+1],nums[right]])
                left += 1
                right -=1
    return result

print(four_sum([2,2,2,2,2,2], 8))
