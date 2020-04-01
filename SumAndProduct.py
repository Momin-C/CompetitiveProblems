#SOURCE: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
from functools import reduce
lst = []
num = [1,2,3]
for i in str(n): lst.append(int(i))
print (reduce(lambda a,b: a*b,lst) - reduce(lambda a,b: a+b ,lst))
