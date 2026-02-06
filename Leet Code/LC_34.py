from collections import Counter

def searchRange(nums, target):
    def findbound(isFirst):
        left = 0
        right = len(nums) - 1
        bound = -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                bound = mid
                if isFirst:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    return [findbound(True), findbound(False)]

print(searchRange([5, 7, 7, 8, 8, 8, 8, 8, 10], 8))
