def containsduplicates(arr,k):
    """Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k"""
    if len(arr)<=0:
        return False

    window = set()
    left = 0

    for i in range(len(arr)):
        current = arr[i]
        if i-left>k:
            window.remove(arr[left])
            left+=1

        if current in window:
            return True
        window.add(current)
    return False

result = containsduplicates([1,2,1,2,2,2],2)
print(result)