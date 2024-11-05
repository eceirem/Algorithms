#polynom: 2x^3 -4x^2 +5x -7

def polynom1(x,A):
    #O(n^2)
    p=0
    for i in range(3, 0, -1):
        temp = 1
        for j in range(i):
            temp *= x
        p = p + A[i] * temp
    p += A[0]
    return p

def polynom2(x,A):
    #O(n)
    p = A[0]
    temp = 1
    for i in range(1, len(A)):
        temp *= x
        p = p + A[i] * temp
    return p


A = [-7, 5, -4, 2]
x = int(input())
result1 = polynom1(x, A)
result2 = polynom2(x, A)
print(result1)
print(result2)