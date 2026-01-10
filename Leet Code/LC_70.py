# Recursive way
# def ways_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return ways_recursive(n - 1) + ways_recursive(n - 2)
#
# print(ways_recursive(10))

#Dynamic Programming
def dp_n(n):
    if n==0:
        return 0
    if n==1:
        return 1

    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]
print(dp_n(5))