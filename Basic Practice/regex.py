# import re
#
# def is_valid(s):
#     try:
#        re.compile(s)
#        return True
#     except re.error:
#         return False
#
# testCases = int(input())
# for _ in range(testCases):
#     str = input()
#     print(is_valid(str))

import re

def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

# Input
n = int(input())
for _ in range(n):
    regex = input()
    print(is_valid_regex(regex))
