num = 2147483647
def isPerfectSquare(num):
    if num ==1 or num ==4 or num ==9:
        return True
    if num%2 ==0:
        start = 2
    else:
        start = 1
    for i in range(start, num//3,2):
        if (i*i == num):
            return True
    return False
print (isPerfectSquare(num))
