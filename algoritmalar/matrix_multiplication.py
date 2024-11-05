def matrix_mul(A, B):
    #O(n^3)
    n1 = len(A) #2
    n2 = len(B[0]) #4
    C = [[0 for i in range(n2)] for j in range(n1)]
    for i in range(n1):
        for j in range(n2):
            for k in range(len(B)): #3
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[2,3,1], [5,2,4]] #2x3
B = [[4,5,1,6], [1,2,1,3], [0,4,1,2]] #3x4
C = matrix_mul(A, B) #2x4
print(C)