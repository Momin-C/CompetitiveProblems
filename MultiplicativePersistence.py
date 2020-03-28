num = input("Input the initial number: ")
length = len(num)
tries = 0
while length != 1:
    product = 1
    for counter in range (length):
        product = product * int(num[counter])
    num = str(product)
    length = len(num)
    tries += 1
print ("It took " + str(tries) + " tries")
