#PROBLEM 917
#SOURCE: https://leetcode.com/problems/reverse-only-letters/
S = "a-bC-dEf-ghIj" #j-Ih-gfE-dCba
def reverseOnlyLetters(S):
    """
    :type S: str
    :rtype: str
    """
    lst = []
    for i in range (S.count("-")):
        print(S.find("-",0))
        lst.append(S.index("-"))
        S = S[:i] + S[i+1:]
        print (S)
    #print (lst)
print (reverseOnlyLetters(S))
