def intersectioOfArray2(nums1, nums2):
    freq = {}

    if len(nums1) < len(nums2):
        for i in nums2:
            freq[i] = freq.get(i, 0) + 1

        result = []
        for num in nums1:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result
    else:
        for i in nums1:
            freq[i] = freq.get(i, 0) + 1

        result = []
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result


print(intersectioOfArray2([9, 4, 9, 8, 4],[4, 9, 5]))

# if len(nums2) < len(nums1):
#     for num in nums2:
#         if num in nums1:
#             nums1.remove(num)
#             result.append(num)
#     return result
# else:
#     for num in nums1:
#         if num in nums2:
#             nums2.remove(num)
#             result.append(num)
#     return result
