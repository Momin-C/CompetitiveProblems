#SOURCE: https://leetcode.com/problems/unique-morse-code-words/
#WORK IN PROGRESS
words = ["gin", "zen", "gig", "msg"]
def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for i in range (len(words)):
        words[i] = list(words[i])
        print(words)
        for x in range (len(words[i])):
            ascii = ord(words[i][x]) - 97
            words[i][x] = morse[ascii]
    return words
print(uniqueMorseRepresentations(words))
