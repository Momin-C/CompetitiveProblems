#PROBLEM 1221
#SOURCE: https://leetcode.com/problems/split-a-string-in-balanced-strings/
s = "RLRRLLRLRL" #4
def balancedStringSplit(s):
    count = 0
    total = 0
    for i in range (len(s)):
        if s[i] == 'R':
            count+=1
        else:
            count-=1
        if count == 0:
            total+=1
    return total
print (balancedStringSplit(s))
