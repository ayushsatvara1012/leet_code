import re
def validPalindrome(s):
    new_str = re.sub(r'[^a-zA-Z0-9]','',s).lower()
    start = 0
    end = len(new_str) - 1

    while start <= end:
        if new_str[start] != new_str[end]:
            return False
        start += 1
        end-=1
    return True
print(validPalindrome('A man, a plan, a canal: Panama'))
