from functools import cmp_to_key

def largest_number(nums):
    """generate the largest number by rearranging the given list of nums"""
    new_str = list(map(str,nums))
## more optimised version give time complexity of O(n)
    new_str.sort(key=cmp_to_key(lambda a,b: -1 if a+b>b+a else 1))
    if new_str[0]=='0':
        return 0

## older version give time complexity of O(n^2)
    # for _ in range(len(nums)-1):
    #     left  = 0
    #     right = left+1
    #     while right < len(nums):
    #         if (new_str[left]+new_str[right]) < (new_str[right]+new_str[left]):
    #             new_str[left],new_str[right] = new_str[right],new_str[left]
    #         left += 1
    #         right += 1
    # if new_str[0] == '0':
    #     return '0'
    #
    return ''.join(new_str)


print(largest_number([3,3,4,43,23,23,23,23]))
