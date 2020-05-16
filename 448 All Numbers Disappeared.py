#PROBLEM 448
#SOURCE: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
nums = [4,3,2,7,8,2,3,1] #[5,6]
def findDisappearedNumbers(nums):
    lst = []
    reduced = set(nums)
    for i in range(1,len(nums)+1):
        if i not in reduced:
            lst.append(i)
    return lst
print (findDisappearedNumbers(nums))
