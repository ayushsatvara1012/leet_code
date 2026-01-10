def longEvenOddSub(nums,threshold):
    i=0
    max_length = 0
    n = len(nums)

    while i<n:
        if nums[i]%2 != 0 or nums[i]>threshold:
            i+=1
            continue
        length = 1
        j = i+1

        while j<n and nums[j]<threshold and nums[j]%2!=nums[j-1]%2:
            length+=1
            j+=1
        max_length = max(max_length,length)
        i=j

    return max_length


res = longEvenOddSub([1,2,3,4,5,6],7)
print(res)