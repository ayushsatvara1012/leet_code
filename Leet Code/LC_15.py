def three_sum(nums):
	"""The time complexity for this code is O(n^3) because of the combinations ([],3)"""
	# seen=set()
	# result = []
	# for tri in combinations(nums,3): # TIme complexity O(n^3)
	# 	if sum(tri)==0:
	# 		sorted_tri = tuple(sorted(tri))
	# 		if sorted_tri not in seen:
	# 			seen.add(sorted_tri)
	# 			result.append(list(sorted_tri))
	# return result

	nums.sort()
	result = []
	for i in range(len(nums)):
		if nums[i] > 0:
			break

		if i > 0 and nums[i] == nums[i - 1]:
			continue

		left = i + 1
		right = len(nums) - 1

		while left < right:
			total = nums[i] + nums[left] + nums[right]
			if total < 0:
				left += 1
			elif total > 0:
				right -= 1
			else:
				result.append([nums[i], nums[left], nums[right]])
				while left < right and nums[right] == nums[right - 1]:
					right -= 1
				while left < right and nums[left] == nums[left + 1]:
					left += 1
				left += 1
				right -= 1
	return result

print(three_sum([-1, 0, 1, 2, -1, -4]))
