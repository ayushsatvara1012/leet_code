from collections import Counter

#
# def xsumArray(nums,k,x):
#
#     start = 0
#     new_list = []
#     for end in range(len(nums)):
#         if end-start+1 == k:
#
#             count_num = Counter(nums[start:end+1])
#
#             sorted_ele = sorted(count_num.items(),key=lambda item:(item[1],item[0]),reverse=True)
#             curr_sum = 0
#             for i in range(min(x,len(sorted_ele))):
#                 ele,freq = sorted_ele[i]
#                 curr_sum += ele*freq
#
#             new_list.append(curr_sum)
#             start+=1
#
#     return new_list
# print(xsumArray([3,8,7,8,7,5],2,2))

##### More optimzed version

def xSumArray(nums,k,x):

    if k>len(nums):
        return []

    result = [0]*((len(nums)-k)+1)
    window = Counter(nums[:k])

    def calc_x(win):
        top_x = sorted(win.items(),key=lambda item:(item[1],item[0]),reverse=True)[:x]
        return sum(ele*freq for ele,freq in top_x)

    result[0]=calc_x(window)



    for i in range(k,len(nums)):

        left_ele = nums[i-k]
        window[left_ele] -= 1
        if window[left_ele]==0:
            del window[left_ele]

        window[nums[i]] += 1
        result[(i-k)+1]=calc_x(window)

    return result
print(xSumArray([1,1,2,2,3,4,2,3],6,2))