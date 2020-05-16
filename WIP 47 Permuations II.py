#PROBLEM 47
#SOURCE: https://leetcode.com/problems/permutations-ii/
nums = [1,1,2]
def permuteUnique(nums):
    lst = []
    q = len(nums)
    for i in range(len(nums)):
        if (nums[i:] + nums[:i]) not in lst:
            lst.append(nums[i:] + nums[:i])
    return lst
print (permuteUnique(nums))
