def topkelements(nums,k):
    freq = {}
    for char in nums:
        freq[char] = freq.get(char, 0) + 1
    result = sorted([(i,j) for i,j in freq.items()],key=lambda item:(item[1]),reverse=True)
    res = [i[0] for i in result]
    print(res[:k])


print(topkelements([1,1,1,0,0,4,3,3,3,3],3))
