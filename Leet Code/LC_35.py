def find_target_index(nums, target):
	left = 0
	right = len(nums) - 1

	while left <= right:  # 0<3
		mid = (right + left) // 2  # 1
		if nums[mid] == target:  # 3 != 2
			return mid
		elif nums[mid] < target:  # 3 < 2
			left = mid + 1
		else:
			right = mid - 1  # 0
	return left


print(find_target_index([1, 3, 4, 5], 7))
