def longestsubstring(s, k):
    """Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.if no such substring exists, return 0."""
    if len(s) < k:
        return 0
    freq = {}
    for char in s:
        freq[char] = freq.get(char,0)+1

    for char in freq:
        if freq[char]<k:
            return max(longestsubstring(part,k) for part in s.split(char))
    return len(s)
print(longestsubstring('aacbaaa', 3))
