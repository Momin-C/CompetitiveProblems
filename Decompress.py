#PROBLEM: 1313
#SOURCE: https://leetcode.com/problems/decompress-run-length-encoded-list/submissions/
nums = [1,2,3,4]
def decompressRLElist(nums):
    lst = []
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range (1,len(nums),2):
        lst.extend([nums[i]] * nums[i-1])
    return lst
print(decompressRLElist(nums))
