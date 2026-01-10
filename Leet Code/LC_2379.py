from collections import Counter

def minRecolors(block,k):

    # recolor = float('inf')
    # for i in range(len(block)-k+1):
    #     window = block[i:i+k]
    #     cnt_w = Counter(window)
    #     no_of_w = cnt_w.get('W',0)
    #     recolor = min(recolor,no_of_w)
    # return recolor

    window_count = block[:k].count('W')
    min_recolor = window_count

    for i in range(k,len(block)):
        if block[i-k] == 'W':
            window_count -= 1
        if block[i] =='W':
            window_count +=1
        min_recolor = min(min_recolor,window_count)
    return min_recolor



res = minRecolors('WBWBWWBWBWBW',2)
print(res)