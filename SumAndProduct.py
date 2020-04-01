#SOURCE: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
n = 4421
product,Sum = 1,0
for i in str(n):
    product *= int(i)
    Sum += int(i)
print (product - Sum)
