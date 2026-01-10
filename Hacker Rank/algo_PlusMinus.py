def plusMinus(arr):
    # Write your code here
    cnt_pos = 0
    cnt_neg = 0
    cnt_zeros = 0
    len_arr = len(arr)
    for number in arr:
        if number<0:
            cnt_neg+=1
        elif number>0:
            cnt_pos+=1
        elif number==0:
            cnt_zeros+=1
    print(f'{(cnt_pos/len_arr):.6f}')
    print(f'{(cnt_neg/len_arr):.6f}')
    print(f'{(cnt_zeros/len_arr):.6f}')