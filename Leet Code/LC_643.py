def findMaxAverage(nums, k):
    """Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted."""
    if len(nums)<0:
        return 0
    result = []
    window_sum = 0

    for i in range(len(nums)):
        window_sum += nums[i]
        if i>= k-1:
            result.append(window_sum/k)
            window_sum -= nums[i-k+1]
    max_avg = f'{max(result):.5f}'
    print(max_avg)
findMaxAverage([1,12,-5,-6,50,3],4)