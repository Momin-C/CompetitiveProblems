#SOURCE: https://leetcode.com/problems/longest-common-prefix/
strs = ["dog","dogaracecar","dcarss","dogman"]
def longestCommonPrefix(strs):
    if len(strs)==0:
        return ""
    strs.sort()
    i = 0
    while (strs[0][i] == strs[-1][i]) and (i < len(strs[0])):
        i += 1
    return strs[0][:i]
print(longestCommonPrefix(strs))
