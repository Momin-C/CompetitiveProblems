#PROBLEM 1389
#SOURCE: https://leetcode.com/problems/create-target-array-in-the-given-order/
nums = [0,1,2,3,4]
index = [0,1,2,2,1]

def createTargetArray(nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
    lst = []
    for i in range (len(nums)):
        lst.insert(index[i],nums[i])
    return lst
print (createTargetArray(nums, index))
