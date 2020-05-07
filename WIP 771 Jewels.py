#SOURCE: https://leetcode.com/problems/jewels-and-stones/
def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    J = "aA"
    S = "aAAbbbb"
    oc = 0
    for i in range (len(S)):
        J = J[1:] + J[0]
        if J in S:
            oc +=1
        if S[i] in J:
            oc+=1
    return (oc)
print (numJewelsInStones("aA","aAAbbbb"))
