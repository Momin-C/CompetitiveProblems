#PROBLEM 1309
#SOURCE: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
s = "10#11#12" #jkab
def freqAlphabets(s):
    w = ""
    i = 0
    while len(s)!=0:
        if len(s)>=2:
            print (s)
            if s[:3]=="10#":
                w+="j"
                s = s[3:]
            elif s[:3]=="11#":
                w+="k"
            elif s[:3]=="12#":
                w+="l"
            elif s[:3]=="13#":
                w+="m"
            elif s[:3]=="14#":
                w+="n"
            elif s[:3]=="15#":
                w+="o"
            elif s[:3]=="16#":
                w+="p"
            elif s[:3]=="17#":
                w+="q"
            elif s[:3]=="18#":
                w+="r"
            elif s[:3]=="19#":
                w+="s"
            elif s[:3]=="20#":
                w+="t"
            elif s[:3]=="21#":
                w+="u"
            elif s[:3]=="22#":
                w+="v"
            elif s[:3]=="23#":
                w+="w"
            elif s[:3]=="24#":
                w+="x"
            elif s[:3]=="25#":
                w+="y"
            elif s[:3]=="26#":
                w+="z"
            s = s[3:]
        if s[0] == "1":
            w+='a'
            s= s[1:]
        elif s[0] == "2":
            w+='b'
            s= s[1:]
        elif s[0] == "3":
            w+='c'
            s= s[1:]
        elif s[0] == "4":
            w+='d'
            s= s[1:]
        elif s[0] == "5":
            w+='e'
            s= s[1:]
        elif s[0] == "6":
            w+='f'
            s= s[1:]
        elif s[0] == "7":
            w+='g'
            s= s[1:]
        elif s[0] == "8":
            w+='h'
            s= s[1:]
        elif s[0] == "9":
            w+='i'
            s= s[1:]
    return w
print(freqAlphabets(s))
