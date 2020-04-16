#SOURCE: https://leetcode.com/problems/keyboard-row/
words = ["Qweyr", "Alaska", "Dad", "Peace"]
def findWords (words):
    row1U = ["Q","W","E","R","T","Y","U","I","O","P"]
    #row1U = ["q","w","e","r","t","y","u","i","o","p"]
    row2U = ["A","S","D","F","G","H","J","K","L"]
    #row2L = ["a","s","d","f","g","h","j",""]
    row3U = ["Z","X","C","V","B","N","M"]

    for i in words:
        for x in range (len(i)):
            if (i.upper())[x] in row1U:
                print ("HI!")

print (findWords(words))
