def make_alternate(s):
    pt1 = 0
    for i in range(len(s)):
        exp= '0' if i%2==0 else '1'
        if s[i]!= exp:
            pt1 += 1
    pt2 = len(s)-pt1
    return min(pt1,pt2)

print(make_alternate("10010100"))