arr = [-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19]
def uniqueOccurrences(arr):
    lst = []
    for i in list(set(arr)):
        lst.append(arr.count(i))
    return True if sorted(set(lst)) == sorted(lst) else False
print (uniqueOccurrences(arr))
