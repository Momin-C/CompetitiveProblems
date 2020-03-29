text = "   HELLO!!11 MY NAME IS MOMIN!!!   "
num = ["0","1","2","3","4","5","6","7","8","9"]
counter = 0
length = len(text)
text = text.strip()
while counter < length:
    length = len(text)
    print (counter)
    if text[counter] != "1":
        text = text[1:]
    print (text)
