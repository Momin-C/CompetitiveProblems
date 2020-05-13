#PROBLEM 804
#SOURCE: https://leetcode.com/problems/unique-morse-code-words/
words = ["gin", "zen", "gig", "msg"]
def uniqueMorseRepresentations(words):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    translated = set([])
    for i in words:
        morseWord = ""
        for x in range(len(i)):
            morseWord+= morse[letters.index(i[x])]
        translated.add(morseWord)
    return len(translated)
print(uniqueMorseRepresentations(words))
