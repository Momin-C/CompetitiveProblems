#PROBLEM 500
#SOURCE: https://leetcode.com/problems/keyboard-row/
words = ["Hello", "Alaska", "Dad", "Peace"]
def findWords (words):
    row1 = "qwertyuiopQWERTYUIOP"
    row2 = "asdfghjklASDFGHJKL"
    row3= "zxcvbnmZXCVBNM"
    onerow = []
    for i in range (len(words)):
        lst = set()
        for x in range(len(words[i])):
            if words[i][x] in row1:
                lst.add(1)
            elif words[i][x] in row2:
                lst.add(2)
            else:
                lst.add(3)
        if len(lst) == 1:
            onerow.append(words[i])
    return onerow
print (findWords(words))
