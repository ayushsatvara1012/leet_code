def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    print(sum(sorted_arr[:-1]),sum(sorted_arr[1:]))