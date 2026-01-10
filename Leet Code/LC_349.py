def intersection(nums1,nums2):
	set_num1 = set(nums1)
	set_num2 = set(nums2)
	result = []
	if set_num1 < set_num2:
		for num in set_num1:
			if num in set_num2:
				result.append(num)
	else:
		for num in set_num2:
			if num in set_num1:
				result.append(num)
	return result
print(intersection([1,2,2,1],[2,2]))