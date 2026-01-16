def longest_palindrome_substring(s):
    """THere are two ways you can do :
    1. Brute force
    2. Ripple algorithm
    """

    # --------------------------------- Ripple algo --------------------------------- #
    def expand(s:str,left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = end = 0
    for center in range(len(s)):
        # for odd length
        len1 = expand(s,center, center)
        # for even length
        len2 = expand(s,center, center + 1)

        curr_max = max(len1,len2)
        if curr_max > end - start:
            start = center - (curr_max - 1) // 2
            end = center + curr_max // 2
    return s[start:end + 1]

    # --------------------------------- Brute Force --------------------------------- #

    # if len(s) < 2:
    #     return s
    # max_len = float('-inf')
    # curr_s = ''
    #
    # for left in range(len(s) - 1):
    #     right = len(s) - 1
    #     while left <= right:
    #         window = s[left:right + 1]
    #         curr_len = len(window)
    #         if s[left] == s[right] and window[::-1] == window and curr_len > max_len:
    #             max_len = curr_len
    #             curr_s = window
    #         right -= 1
    # return curr_s

print(longest_palindrome_substring('acbbdddyyyyyyyyy'))
