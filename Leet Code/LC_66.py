def plusOne(digits):
    return ([i for i in str((int(''.join(map(str,digits))))+1)])
print(plusOne([1,2,3]))