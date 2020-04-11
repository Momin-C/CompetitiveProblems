#SOURCE: https://leetcode.com/problems/basic-calculator-ii/
strr = " 3  *      2/4 "

lst = (list(filter(lambda x: x != " ",strr)))
i = 0

if "/" in lst:
    index = lst.index("/")
    q = (int(lst[index-1]))/(int(lst[index+1]))
print (q)
