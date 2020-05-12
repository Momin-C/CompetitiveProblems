#PROBLEM 136
#SOURCE: https://leetcode.com/problems/single-number/
nums = [2,2,1] #1
def singleNumber(nums):
    numbers = set([])
    for i in nums:
        if i in numbers:
            numbers.remove(i)
        else:
            numbers.add(i)
    return numbers.pop()
print (singleNumber(nums))
