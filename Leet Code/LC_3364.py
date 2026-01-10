l = 2
r = 4
nums = [1, 2, 3, 4]
n = len(nums)
if l > n:
    print(-1)
start = 0
min_sum = float('inf')
curr_sum = 0

for length in range(l, r + 1):
    curr_sum = sum(nums[:length])
    if curr_sum > 0:
        min_sum = min(min_sum, curr_sum)

    for end in range(length, n):
        curr_sum += nums[end] - nums[end - length]
        if curr_sum > 0:
            min_sum = min(min_sum, curr_sum)
print(min_sum if min_sum != float('inf') else -1)


#### More optimised version


def minSumSubarray(nums, l, r):
    n = len(nums)
    if l > n:
        return -1

    result = float('inf')

    for length in range(l, r + 1):
        s = sum(nums[:length])
        if 0 < s < result:
            result = s

        for i in range(length, n):
            s += nums[i] - nums[i - length]
            if 0 < s < result:
                result = s

    return -1 if result == float('inf') else result
