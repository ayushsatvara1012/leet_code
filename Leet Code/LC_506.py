from collections import defaultdict


def relativeRank(nums):
    score_to_index = defaultdict(int)
    n=len(nums)
    for i in range(n):
        score_to_index[nums[i]] = i
    nums.sort(reverse=True)

    rank = ['']*n
    for j in range(n):
        if j == 0:
            rank[score_to_index[nums[j]]]='Gold Medal'
        elif j == 1:
            rank[score_to_index[nums[j]]]='Silver Medal'
        elif j == 2:
            rank[score_to_index[nums[j]]]='Bronze Medal'
        else:
            rank[score_to_index[nums[j]]]= str(j+1)
    return rank


print(relativeRank([10, 2, 33, 5, 1]))
