#PROBLEM 1436
#SOURCE: https://leetcode.com/problems/destination-city/
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
def destCity(paths):
    start = [x[0] for x in paths]
    end = [x[1] for x in paths]
    for i in end:
        if i not in start:
            return i
print (destCity(paths))
