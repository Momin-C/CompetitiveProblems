#SOURCE: https://leetcode.com/problems/intersection-of-two-arrays-ii/
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        big = nums1
        small = nums2
    else:
        big = nums2
        small = nums1

    lst = []
    for i in range (len(small)):
        if small[i] in big:
            lst.append(small[i])
            del big [big.index(small[i])]
    return lst

print (intersect(nums1,nums2))
