A = [[1,1,0],[1,0,1],[0,0,0]]
def flipAndInvertImage(A):
    for i in range(len(A)):
        A[i] = A[i][::-1]
        for x in range(len(A[i])):
            if A[i][x] == 1:
                A[i][x] = 0
            else:
                A[i][x] = 1
    return A
print (flipAndInvertImage(A))
