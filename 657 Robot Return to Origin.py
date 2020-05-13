#PROBLEM 657
#SOURCE: https://leetcode.com/problems/robot-return-to-origin/
moves = "RRUU" #False
def judgeCircle(moves):
    x,y = 0,0
    for i in range(len(moves)):
        if moves[i] == "U":
            y+=1
        elif moves[i] == "D":
            y-=1
        elif moves[i] == "R":
            x+=1
        else:
            x-=1
    return (x==0 and y==0)
print (judgeCircle(moves))
