#PROBLEM 1299
#SOURCE: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
arr = [17,18,5,4,6,1]

def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    for i in range(len(arr)):
        if i!= len(arr)-1:
            arr[i] = max(arr[i+1:])
    arr[-1] = -1
    return arr

print (replaceElements(arr))
