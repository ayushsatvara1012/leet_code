def isHappy(n):
    happy_num = n
    seen = set()
    while happy_num != 1:
        if happy_num in seen:
            return False
        seen.add(happy_num)
        happy_num = sum(int(i) ** 2 for i in str(happy_num))
    return True
print(isHappy(55))