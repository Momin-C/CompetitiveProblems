#SOURCE: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
n=7
def generateTheString(n):
    return ("a"*(n-1)+"b") if n%2==0 else ("a"*n)
print (generateTheString(n))
