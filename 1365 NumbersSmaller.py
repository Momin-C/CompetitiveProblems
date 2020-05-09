#PROBLEM 1365
#SOURCE: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
nums = [7,7,7,7]
def smallerNumbersThanCurrent(nums):
    lst = []
    for i in range (len(nums)):
        oc = 0
        for x in range (len(nums)):
            if nums[i] > nums[x]:
                oc +=1
        lst.append(oc)
    return lst
print (smallerNumbersThanCurrent(nums))
