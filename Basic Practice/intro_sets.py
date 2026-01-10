def average(array):
    setArr = set(array)
    lenArr = len(setArr)
    total = 0
    newarr = list(setArr)
    for i in range(lenArr):
        total = total + newarr[i]
    return total/lenArr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# input : 161 182 161 154 176 170 167 171 170 174