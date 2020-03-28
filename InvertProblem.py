x = int(input())

x = str(x)

if x[0] != "-":
    x = x[::-1]
    print (x)
elif x[0] == "-":
    x = x[1:]
    x = x[::-1]
    x = "-" + x
x = int(x)

if (x>2**31-1) or (x<-2**31):
    print (0)
else:
    print (x)
