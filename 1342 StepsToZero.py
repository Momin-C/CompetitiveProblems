#PROBLEM 1342
#SOURCE: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
num = 14
def numberOfSteps (num):
    count = 0
    while num!= 0:
        if num%2 == 0:
            num/=2
        else:
            num-=1
        count +=1
    return (count)
print (numberOfSteps(num))
