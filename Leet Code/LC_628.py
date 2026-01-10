def maxProdOfThree(nums):
    return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])

print(maxProdOfThree([-100,-98,-1,2,3,4]))