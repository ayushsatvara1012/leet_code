def diagonalDifference(arr):
    # Write your code here
    lef_rig = 0
    rig_lef = 0
    len_arr = len(arr)
    for row in range(len_arr):
        lef_rig += arr[row][row]
        rig_lef += arr[row][(len_arr-1)-row]
    return abs(lef_rig-rig_lef)