from operator import index, indexOf

def twosum2(nums,target):
    seen = set()
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in seen:
            return [nums.index(comp)+1,i+1]
        seen.add(nums[i])

print(twosum2([-1,0],-1))