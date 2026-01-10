def findTheDifference(s,t):
    freq = {}
    for char in t:
        freq[char] = freq.get(char, 0) + 1

    for char_s in s:
        if char_s in freq and freq[char_s] > 0:
            freq[char_s] -= 1
    return ''.join(key for key,val in freq.items() if val!=0)
print(findTheDifference('abcd','abcdg'))