def staircase(n):
    # Write your code here
    for col in range(1,n+1):
        print(' '* (n-col)+ '#'*col)