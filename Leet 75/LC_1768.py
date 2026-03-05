def merge_strings(word1,word2):
    res = []
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            res.append(word1[i])
        if i < len(word2):
            res.append(word2[i])

    return ''.join(res)


print(merge_strings('abc','pqrst'))