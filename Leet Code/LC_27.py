from collections import Counter

nums = [2, 3, 4, 2, 1, 12, 2, 4, 3, 12, 6,2,2]
val = 2

left = 0
right = len(nums) - 1

while left <= right:
    if nums[left] == val:
        if nums[right]==val:
            right-=1
        else:
            nums[left]=nums[right]
            right-=1
            left += 1
    else:
        left += 1

print(left)
