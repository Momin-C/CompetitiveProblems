#PROBLEM 1
#SOURCE: https://leetcode.com/problems/two-sum/submissions/
def twoSum(nums, target):
    lst = []
    for i in range (len(nums)):
        if abs(nums[i]) > abs(target) and min(nums) >0 and target !=0 and nums[i]>0:
            continue
        diff = target - nums[i]
        if diff in nums[i+1:]:
            if i+1 < len(nums):
                num = (nums.index(diff,i+1))
                lst.extend([i,num])
                break
    return lst
