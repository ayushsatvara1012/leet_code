def longest_substring_k_distinct(s,k):
    """
        Find longest substring with at most k distinct characters.
        s = "araaci", k = 2
        Answer: 4 ("araa")
    """
    char_count = {}
    max_len = 0
    left = 0

    for right in range(len(s)):
        #Expand the right side
        char_count[s[right]] = char_count.get(s[right],0)+1

        #Shrink if condition satisfy
        while len(char_count)>k:
            char_count[s[left]]-=1
            if char_count[s[left]]==0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len,right-left+1)
    return max_len