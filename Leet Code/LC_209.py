def minSubarray(arr, target):
    """Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead."""

    if len(arr) <= 0:
        return 0

    start = 0
    window = 0
    min_len = float('inf')

    for end in range(len(arr)):
        window += arr[end]
        while window >= target:
            min_len = min(min_len, end - start + 1)
            window -= arr[start]
            start += 1

    return min_len if min_len != float('inf') else 0

print(minSubarray([1,4,4], 4))
