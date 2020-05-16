#PROBLEM 442
#SOURCE: https://leetcode.com/problems/find-all-duplicates-in-an-array/
nums = [4,3,2,7,8,2,3,1] #[2,3]
def findDuplicates(nums):
    """
    #SOLUTION 1
    lst = []
    A = set(nums)
    for i in A:
        if nums.count(i) >=2:
            lst.append(i)
    return (lst)
    """
    return [x for x in set(nums) if nums.count(x) >=2]
print (findDuplicates(nums))
