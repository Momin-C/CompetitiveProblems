#PROBLEM 35
#SOURCE: https://leetcode.com/problems/search-insert-position/
def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        for i in range(0,len(nums)-1):
            if nums[i] < target < nums[i+1]:
                return i+1
print (searchInsert([1,3,5,6],7))
