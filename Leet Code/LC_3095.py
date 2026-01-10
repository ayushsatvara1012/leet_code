def shortest_special_subarray(nums,k):
    n = len(nums)
    min_len = float('inf')

    for start in range(n):
        curr = 0
        for end in range(start,n):
            curr |= nums[end]
            if curr>=k:
                min_len = min(min_len,end-start+1)
                break
    return min_len if min_len != float('inf') else -1



print(shortest_special_subarray([2,1,8],110))
