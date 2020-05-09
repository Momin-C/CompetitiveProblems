#PROBLEM 1323
#SOURCE: https://leetcode.com/problems/maximum-69-number/
num = 9999 # 9999

def maximum69Number (num):
    num = str(num)
    return int(str(num).replace("6","9",1))
    """
    r = num.find("6")
    if r != -1:
        return int(num[:r] + "9" + num[r+1:])
    else:
        return int(num)
    """
print (maximum69Number(num))
