A = [-7,-3,2,3,11]
def sortedSquares(A):
    for i in range (len(A)):
        A[i] = A[i]**2
    A.sort()
    return A
print (sortedSquares(A))
