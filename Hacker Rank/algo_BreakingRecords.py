def breakrecords(arr):
    count_high = 0
    count_low = 0
    high_score = arr[0]
    low_score = arr[0]
    for score in arr:
        if score < low_score:
            low_score = score
            count_low += 1
        elif score > high_score:
            high_score = score
            count_high += 1
    print(count_high,count_low)

breakrecords([3 ,4 ,21 ,36, 10 ,28 ,35 ,5 ,24,42])

