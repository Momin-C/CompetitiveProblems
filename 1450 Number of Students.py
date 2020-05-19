#PROBLEM 1450
#SOURCE: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
def busyStudent(startTime, endTime, queryTime):
    count = 0
    for i in range(len(startTime)):
        if startTime[i]<=queryTime<=endTime[i]:
            count+=1

    #SOLUTION 2
    #return sum([1 for i in range(len(startTime)) if startTime[i]<=queryTime<=endTime[i]])
print (busyStudent([1,2,3],[3,2,7],4)) #1
