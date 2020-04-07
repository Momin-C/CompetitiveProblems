morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = ["gin", "zen", "gig", "msg"]
for i in range (len(words)):
    for x in range (len(words[i])):
        letter = words[i][x]
        letter = letter[1:] + morse[x]

    print (letter)
print (words)
