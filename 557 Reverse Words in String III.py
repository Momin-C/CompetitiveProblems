s = "Let's take LeetCode contest" #s'teL ekat edoCteeL tsetnoc
def reverseWords(s):
    mod = s.split(" ")
    string = ""
    for i in range(len(mod)):
        string+=mod[i][::-1] + " "
    return string.strip()
print (reverseWords(s))
