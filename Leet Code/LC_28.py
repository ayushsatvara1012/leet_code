def strStr(haystack,needle):
    if needle in haystack:
        idx = haystack.index(needle)
        return idx
    return -1
print(strStr('leetcode','leeto'))