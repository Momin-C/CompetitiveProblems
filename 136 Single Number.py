#PROBLEM 136
#SOURCE: https://leetcode.com/problems/single-number/
def singleNumber(self, nums):
	for i in nums:
		if nums.count(i) == 1:
			return i
