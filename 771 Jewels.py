#SOURCE: https://leetcode.com/problems/jewels-and-stones/
J = "aA"
S = "aAAbbbb"
oc = 0
for i in range (len(S)):
    J = J[1:] + J[0]
    if J in S:
        oc +=1
    if S[i] in J:
        oc+=1
print (oc)
