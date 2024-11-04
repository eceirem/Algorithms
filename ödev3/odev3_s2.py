import math

def lg(n):
    m = 0
    while pow(2, m) < n: 
        m += 1
    return m

num = int(input())
print(lg(num))
