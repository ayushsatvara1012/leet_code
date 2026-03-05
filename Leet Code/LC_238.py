def buildPrefix(nums):
    prefix = [0]*len(nums)
    prefix[0] = 1

    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1]*nums[i-1]
    return prefix

def buildSuffix(nums):
    n = len(nums)
    suffix = [0]*n
    suffix[n-1] = 1
    for i in range(n-2,-1,-1):
        suffix[i] = suffix[i+1]*nums[i+1]
    return suffix



x =buildPrefix([1,2,3,4])
y =buildSuffix([1,2,3,4])
n = 4 #len(nums)
result= [0]*n
for i in range(n):
    result[i] = x[i]*y[i]
print(result)
