arr = [1,2,2,3,3,3]
def findLucky(arr):
    lst = []
    for i in arr:
        if arr.count(i) == i:
            lst.append(i)
        else:
            lst.append(-1)
    return max(lst)
print (findLucky(arr))
