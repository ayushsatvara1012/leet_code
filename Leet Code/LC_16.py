def three_sum_closest(nums, target):
    """Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
     Return the sum of the three integers."""
    nums.sort()
    final_sum = 0
    min_diff = float('inf')

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            target_sum = nums[i] + nums[left] + nums[right]
            curr_diff = abs(target - target_sum)
            if curr_diff < min_diff:
                final_sum = target_sum
                min_diff = curr_diff
            if target > target_sum:
                left += 1
            elif target < target_sum:
                right -= 1
            else:
                return target_sum
    return final_sum


print(three_sum_closest([-1, 2, 1, 4], 1))
