#SOURCE: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""from functools import reduce
lst = []
n = 1234
for i in str(n): lst.append(int(i))
print (list(filter(lambda a: a%2==0,lst)))
print (lst)
print (list(map(lambda x: x*2,lst)))
print (lst)
#print (reduce(lambda a,b: a*b,lst) - reduce(lambda a,b: a+b ,lst))
temps = [("Berlin",39),("Cairo",23),("Toronto",32)]
print (temps)
temps = (list(map(lambda x: (x[0],x[1]*9/5 + 2),temps)))
print (temps)"""
import statistics
nums = [1.3,2.7,0.8,4.1]
avg = statistics.mean(nums)
greater = list(filter(lambda x: x>avg, nums))
print (greater)
