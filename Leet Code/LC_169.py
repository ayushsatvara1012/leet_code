def majorityElement(nums):
    count = 0
    major = None

    for num in nums:
        if count ==0:
            major = num
        count += (1 if num == major else -1)
    return major
print(majorityElement([2,2,1,2,1,1,2,1,2]))