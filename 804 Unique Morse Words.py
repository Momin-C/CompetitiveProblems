#SOURCE: https://leetcode.com/problems/unique-morse-code-words/
#WORK IN PROGRESS
def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for i in range (len(words)):
        for x in range (len(words[i])):
            letter = words[i][x]
            letter = letter[1:] + morse[x]
            words[i][x] = letter
    return words
words = ["gin", "zen", "gig", "msg"]
print (uniqueMorseRepresentations(words))
