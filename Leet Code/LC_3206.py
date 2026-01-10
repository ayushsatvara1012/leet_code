def alt_group(colors:list[int]):

    n= len(colors)
    if n<3:
        return 0
# Method 1: 57ms Time complexity
    #
    # total = 0
    # prev = colors[-1]
    #
    # for i in range(n):
    #     curr = colors[i]
    #     next_val = colors[(i+1)%n]
    #     if prev == next_val and curr != prev :
    #         total += 1
    #     prev = curr
    # return total

#MEthod 2: 33ms without modulo

    total = 0
    for i in range(1,n-1):
        if colors[i-1]==colors[i+1] and colors[i]!= colors[i-1]:
            total += 1
    if colors[-1]==colors[1] and colors[0]!=colors[-1]:
        total += 1
    if colors[-2]==colors[0] and colors[-1]!=colors[-2]:
        total += 1

    return total


print(alt_group([0,1,0,0,1]))