from itertools import permutations, combinations


def arrayPartition(nums):
    nums.sort()
    max_sum = 0
    for i in range(0,len(nums),2):
        max_sum+=nums[i]
    return max_sum

print(arrayPartition([6,2,6,5,1,2]))


# for i in range(0,len(res),2):
#     print(f'res[i]:{res[i]},res[i+1]:{res[i+1]}')
#     print(min(res[i]),min(res[i+1]))
#     print(len(res))