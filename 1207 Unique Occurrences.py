arr = [-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19]
def uniqueOccurrences(arr):
    lst = []
    mod = list(set(arr))
    for i in mod:
        c = arr.count(i)
        lst.append(c)
    if sorted(set(lst)) == sorted(lst):
        return True
    else:
        return False
print (uniqueOccurrences(arr))
