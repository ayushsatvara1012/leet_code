def columnNumber(s):

    result = 0
    for char in s:
        digit = ord(char)-ord('A')+1
        result = result * 26 + digit
    return result

print(columnNumber('ZY'))