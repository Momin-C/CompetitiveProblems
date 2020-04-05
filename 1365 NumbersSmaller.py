#SOURCE: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
nums = [7,7,7,7]
rtype = []
for i in range (len(nums)):
    oc = 0
    for x in range (len(nums)):
        if nums[i] > nums[x]:
            oc +=1
    rtype.append(oc)
print (rtype)
