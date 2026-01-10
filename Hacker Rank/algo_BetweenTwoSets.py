import math

a = [2,6]
b = [24,36]
def getTotalX(a, b):
    # Write your code here
    lcm_a = math.lcm(*a)
    gcd_b = math.gcd(*b)
    total = 0
    print(lcm_a,gcd_b)
    current = lcm_a
    while current<=gcd_b:
        if gcd_b%current ==0:
            total += 1
        current += lcm_a
    return total

getTotalX(a,b)