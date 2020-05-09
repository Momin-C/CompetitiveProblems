#PROBLEM 977
#SOURCE: https://leetcode.com/problems/squares-of-a-sorted-array/
A = [-7,-3,2,3,11]
def sortedSquares(A):
    """
    for i in range (len(A)):
        A[i] = A[i]**2
    A.sort()
    return A
    """

    """
    return sorted(list(map(lambda x: x**2,A)))
    """

    return sorted([x**2 for x in A])

print (sortedSquares(A))
