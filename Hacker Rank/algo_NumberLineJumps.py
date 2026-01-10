def kangaroo(x1,v1,x2,v2):
# if both kangaroo is at same position and velocities are same then rtn yes else no
    if v1==v2:
        return 'YES' if x1==x2 else 'NO'
# if the kangaroo behind is slower than return no
    if (x1<x2 and v1<=v2) or (x1>x2 and v1>=v2):
        return 'NO'
    if (x1-x2)%(v2-v1)==0:
        n=(x1-x2)//(v2-v1)
        if n>0:
            return 'YES'
    return 'NO'


result = kangaroo(3,0,3,1)
print(result)
