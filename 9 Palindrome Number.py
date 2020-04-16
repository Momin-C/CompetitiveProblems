#SOURCE: https://leetcode.com/problems/palindrome-number/
x = -121
def isPalindrome(x):
    return str(x) == str(x)[::-1]
print (isPalindrome(x))
