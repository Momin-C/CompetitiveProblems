#PROBLEM 344
#SOURCE: https://leetcode.com/problems/reverse-string/
s = ["h","e","l","l","o"]
def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    f = len(s)
    for i in range (len(s)-1,-1,-1):
        s.append(s[i])
    del s[:f]
    return s
print (reverseString(s))
