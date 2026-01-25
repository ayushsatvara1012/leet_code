def zigzag(s, row):
    """Zigzag Conversion"""
    curr_row = 0
    nums_row = row
    dir = 1
    result = [''] * nums_row
    for i in range(len(s)):
        result[curr_row] += s[i]
        if curr_row == 0:
            dir = 1
        elif curr_row == nums_row - 1:
            dir = -1
        curr_row += dir
    return ''.join(result)

print(zigzag('paypalishiring', 3))
