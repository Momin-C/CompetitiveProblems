#PROBLEM 227
#SOURCE: https://leetcode.com/problems/basic-calculator-ii/
s = " 3/2 "

def calculate(self, s):
    lst = (list(filter(lambda x: x != " ",s)))
    while len(lst) >1:
        if "/" in lst:
            where = lst.index("/")
            before = float(lst[where-1])
            after = float(lst[where+1])
            q = before/after
            del lst[where-1:where+2]
            lst.insert(where-1,q)
        if "*" in lst:
            where = lst.index("*")
            before = float(lst[where-1])
            after = float(lst[where+1])
            m = before*after
            del lst[where-1:where+2]
            lst.insert(where-1,m)
        if "+" in lst:
            where = lst.index("+")
            before = float(lst[where-1])
            after = float(lst[where+1])
            p = before+after
            del lst[where-1:where+2]
            lst.insert(where-1,p)
        if "-" in lst:
            where = lst.index("-")
            before = float(lst[where-1])
            after = float(lst[where+1])
            d = before-after
            del lst[where-1:where+2]
            lst.insert(where-1,d)
    return (int(lst[0]))
print (lst)
