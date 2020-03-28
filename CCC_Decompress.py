L = int(input("Input: "))
X = []
for counter in range (L):
    text = input("Num + Character: ")
    if text[1] != " ":
        num = int(text[0:2])
        char = text[3]
    else:
        num = int(text[0])
        char = text[2]
    X.append(num*char)
for counter in range (L):
    print (X[counter])
