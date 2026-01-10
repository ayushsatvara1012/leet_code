def substring3(s):
    total = 0
    for i in range(len(s)-2):
        window = s[i:i+3]
        if len(set(window))==3:
            total += 1
    return total
res = substring3('xyzzazazssyszx')
print(res)
