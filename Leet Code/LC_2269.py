def kbeauty(nums,k):
    """- "24" from "240": 24 is a divisor of 240.
        "40" from "240": 40 is a divisor of 240.
        Therefore, the k-beauty is 2."""
    k_beauty = 0
    new_num = str(nums)
    for i in range(len(new_num)-k+1):
        window = int(new_num[i:i+k])
        if window!=00 and nums%window == 0:
            k_beauty+=1
    return k_beauty
result = kbeauty(430043,2)
print(result)
