#PROBLEM 215
#SOURCE: https://leetcode.com/problems/kth-largest-element-in-an-array/
nums = [3,2,1,5,6,4]
k = 2
def findKthLargest(nums, k):
    nums.sort(reverse = True)
    return nums[k-1]
print(findKthLargest(nums,k)) #5
