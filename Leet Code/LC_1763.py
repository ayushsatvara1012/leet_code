def niceString(s):
    n= len(s)
    def nice(substring):
        char_set = set(substring)
        for char in char_set:
            if char.lower() not in char_set or char.upper() not in char_set:
                return False
        return True

    longest = ''
    for i in range(n):
        for j in range(1,n+1):
            sub_string = s[i:j]
            if nice(sub_string):
                if len(sub_string)>len(longest):
                    longest = sub_string
    return longest
result  = niceString('YazaAayYaaZ')
print(result)