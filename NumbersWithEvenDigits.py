#SOURCE: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
nums = [12,345,2,6,7896]
oc = 0
for i in nums:
    if len(str(i))%2 ==0: oc+=1
return oc
