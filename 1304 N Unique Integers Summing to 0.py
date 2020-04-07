#SOURCE: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
n = 3
def sumZero(n):
    lst = []
    if n%2 != 0:
        lst = [0]
    for i in range (1,int(n/2)+1):
        lst.extend([i,i*-1])
    return lst
print (sumZero(3))
