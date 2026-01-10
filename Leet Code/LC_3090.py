from collections import defaultdict

s='bcbcbabcbabcb'
max_length = 0
left = 0

freq = {}

for right in range(len(s)):
    char = s[right]
    freq[char] = freq.get(char,0)+1

    while freq[char]>2:
        freq[s[left]]-=1
        left+=1
    max_length = max(max_length,right-left+1)
print(max_length)


