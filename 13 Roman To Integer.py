#SOURCE: https://leetcode.com/problems/roman-to-integer/
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    i = len(sum)-1
    while len(sum) != 0:
        i-=1
        if s[i:i+2] == "IV":
            sum+=4
        elif s[i:i+2] == "IX":
            sum+=9
        elif s[i:i+2] == "XL":
            sum+=40
        elif s[i:i+2] == "XC":
            sum+=90
        elif s[i:i+2] == "CD":
            sum+=400
        elif s[i:i+2] == "CM":
            sum+=900
    return s[0]
print (romanToInt("Hello!"))
