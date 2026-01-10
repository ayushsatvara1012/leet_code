import math


def maxLength(nums):
    """Input: nums = [1,2,1,2,1,1,1]"""
    max_len = 0
    start = 0

    for end in range(len(nums)):
        while start <= end:
            window = nums[start:end + 1]
            if len(window) == 0:
                break

            prod_val = math.prod(window)
            lcm_val = math.lcm(*window)
            gcd_val = math.gcd(*window)

            if prod_val == lcm_val * gcd_val:
                max_len = max(max_len, end - start + 1)
                break
            else:
                start += 1
        if start > end:
            start = end

    return max_len


print(maxLength([2, 3, 4, 5, 6]))
