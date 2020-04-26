#SOURCE: https://leetcode.com/problems/roman-to-integer/
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    i=0
    while len(s)!=0:
        if s[i:i+2] == "IV":
            sum+=4
            s = ("."*i) + s[i+2:]
        elif s[i:i+2] == "IX":
            sum+=9
            i+=2
            s = ("."*i) + s[i+2:]
        elif s[i:i+2] == "XL":
            sum+=40
            i+=2
            s = ("."*i) + s[i+2:]
        elif s[i:i+2] == "XC":
            sum+=90
            i+=2
            s = ("."*i) + s[i+2:]
        elif s[i:i+2] == "CD":
            sum+=400
            i+=2
            s = ("."*i) + s[i+2:]
        elif s[i:i+2] == "CM":
            sum+=900
            i+=2
            s = ("."*i) + s[i+2:]
        elif s[i] == "I":
            sum+=1
        elif s[i] == "V":
            sum+=5
        elif s[i] == "X":
            sum+=10
        elif s[i] == "L":
            sum+=50
        elif s[i] == "C":
            sum+=100
        elif s[i] == "D":
            sum+=500
        elif s[i] == "M":
            sum+=1000
        i+=1
        print (i)
        print (sum)
    return sum
print (romanToInt("LVIII"))
