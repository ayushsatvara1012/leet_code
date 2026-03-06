def kids_candies(candies,extra_candies):
    greatest = max(candies)
    res = []
    for i in range(len(candies)):
        ext = extra_candies + candies[i]
        res.append(ext>=greatest)
    return res

print(kids_candies([4,2,1,1,2],1))