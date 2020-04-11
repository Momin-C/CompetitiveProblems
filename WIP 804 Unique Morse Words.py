#SOURCE: https://leetcode.com/problems/unique-morse-code-words/
#WORK IN PROGRESS
def uniqueMorseRepresentations(words):
    morseWord = ""
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for i in range (len(words)):
        words[i] = list(words[i])
        for x in range (len(words[i])):
            words[i][x] = morse[x]
        print (words)
    return words
#words = ["gin", "zen", "gig", "msg"]
words = ["aaa","Hi"]
print (uniqueMorseRepresentations(words))
