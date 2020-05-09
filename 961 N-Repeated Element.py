#PROBLEM 961
#SOURCE: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
A = [1,2,3,3]
def repeatedNTimes(A):
    for i in A:
        if A.count(i) >1: return i

    """
    return (list(filter(lambda x: A.count(x) >1,A)))[0] //TIMES OUT
    """

    """
    return [x for x in A if A.count(x) >1][0] //TIMES OUT
    """
print (repeatedNTimes(A))
