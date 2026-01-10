def min_len_arr(nums,k):
	min_len = float('inf')
	left = 0
	freq = {}
	curr_sum = 0
	for right in range(len(nums)):
		num = nums[right]
		curr_sum += num
		freq[num] = freq.get(num, 0) + 1

		if freq[num]>1:
			freq[num]-=1
			left += 1
			curr_sum -= num
		while curr_sum>=k:
			min_len = min(min_len,right-left+1)
			left += 1
			curr_sum -= nums[left]

	return min_len if min_len != float('inf') else -1

print(min_len_arr([5,5,4],5))
