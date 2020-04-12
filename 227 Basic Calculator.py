#SOURCE: https://leetcode.com/problems/basic-calculator-ii/
s = " 3/2 "

lst = (list(filter(lambda x: x != " ",s)))
def operation(sign):
    where = lst.index(sign)
    before = float(lst[where-1])
    after = float(lst[where+1])
    if sign == "/":
        q = before/after
    elif sign == "*":
        q = before*after
    elif sign == "+":
        q = before+after
    elif sign == "-":
        q = before-after
    lst.insert(where-1,q)
    del lst[where-1:where+2]
while len(lst) >1:
    if "/" in lst:
        operation("/")
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
print (lst)
