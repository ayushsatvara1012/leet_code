def countApplesAndOranges(s, t, a, b, apples, oranges):
    # total_apple =total_orange = 0
    # for apple in apples:
    #     dist_apple = a + apple
    #     if s<=dist_apple<=t:
    #         total_apple += 1
    # for orange in oranges:
    #     dist_orange = b + orange
    #     if s<=dist_orange<=t:
    #         total_orange += 1
    total_apples = sum(1 for apple in apples if s<=a+apple<=t)
    total_oranges = sum(1 for orange in oranges if s<=b+orange<=t)
    print(total_apples)
    print(total_oranges)
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])