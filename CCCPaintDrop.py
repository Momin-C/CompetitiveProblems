#PROBLEM: https://cemc.uwaterloo.ca/contests/computing/2020/stage%201/juniorEF.pdf

L = int(input("Num of lines: "))
drops = []
dropsX = []
dropsY = []
for counter in range (L):
    paintdrop = input("Input coordinates: ")
    drops.append(paintdrop)
for counter in range (0,L,2):
    dropsX.append(drops[counter])
for counter in range (1,L,2):
    dropsY.append(drops[counter])
print (dropsX)
print (dropsY)
