#PROBLEM 1346
#SOURCE: https://leetcode.com/problems/check-if-n-and-its-double-exist/
arr = [-2,0,10,-19,4,6,-8]
def checkIfExist(arr):
    if arr.count(0) > 1:
        return True
    for i in arr:
        if (i/2 in arr or i*2 in arr) and (i!=0):
            return True
    return False
print(checkIfExist(arr))
