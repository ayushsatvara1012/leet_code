def sliding_Window_fixed_length(arr,k):
    """
        Find maximum sum of any k consecutive elements.
        arr = [2, 1, 5, 1, 3, 2], k = 3
        Windows: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6
        Answer: 9
    """
    if len(arr)<k:
        return None

    # Step 1: calculate the first window[0:k-1]
    window = sum(arr[:k])
    max_sum = window

    # Step 2: slide the window one step at a time
    for rp in range(k,len(arr)):
        window = window - arr[rp-k] + arr[rp]
        max_sum = max(max_sum,window)

    return max_sum

print(sliding_Window_fixed_length([1,4,3,7,2,3,4],3))