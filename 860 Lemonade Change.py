#WIP
#PROBLEM 860
#SOURCE: 
bills = [10,10] #False
def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    m = 0
    for i in range (len(bills)):
        m+=bills[i]
        if bills[i]>5:
            print (i, m + 5 - bills[i])
            m = m + 5 - bills[i]

        if m<0:
            return False
    return True
print (lemonadeChange(bills))
