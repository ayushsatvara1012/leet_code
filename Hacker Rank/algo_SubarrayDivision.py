# [ 1 2 1 3 2 ]
def subdivison(arr,d,m):
    squares = 0
    if len(arr)<0:
        return 0

    window_sum = sum(arr[:m])
    if window_sum == d:
        squares += 1

    for i in range(m,len(arr)):
        window_sum = window_sum - arr[i-m] + arr[i]
        if window_sum == d:
            squares += 1
    print(squares)


subdivison([1,2,1,3,2],3,2)