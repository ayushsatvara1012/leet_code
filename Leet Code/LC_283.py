def moveZeros(nums):
	left = 0
	for right in range(len(nums)):
		if nums[right] != 0:
			key = nums[right]
			pos = left

			while pos > 0 and key < nums[pos]:
				nums[pos] = nums[pos-1]


print(moveZeros([1, 0, 3, 12, 0, 0, 5]))
