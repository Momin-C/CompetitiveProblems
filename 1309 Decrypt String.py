#PROBLEM 1309
#SOURCE: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
s = "10#11#12" #jkab
def freqAlphabets(s):
    w = ""
    i = 0
    while len(s)!=0:
        if len(s)>=2:
            if s[:3]=="10#":
                w+="j"
                s = s[3:]
            elif s[:3]=="11#":
                w+="k"
                s = s[3:]
            elif s[:3]=="12#":
                w+="l"
                s = s[3:]
            elif s[:3]=="13#":
                w+="m"
                s = s[3:]
            elif s[:3]=="14#":
                w+="n"
                s = s[3:]
            elif s[:3]=="15#":
                w+="o"
                s = s[3:]
            elif s[:3]=="16#":
                w+="p"
                s = s[3:]
            elif s[:3]=="17#":
                w+="q"
                s = s[3:]
            elif s[:3]=="18#":
                w+="r"
                s = s[3:]
            elif s[:3]=="19#":
                w+="s"
                s = s[3:]
            elif s[:3]=="20#":
                w+="t"
                s = s[3:]
            elif s[:3]=="21#":
                w+="u"
                s = s[3:]
            elif s[:3]=="22#":
                w+="v"
                s = s[3:]
            elif s[:3]=="23#":
                w+="w"
                s = s[3:]
            elif s[:3]=="24#":
                w+="x"
                s = s[3:]
            elif s[:3]=="25#":
                w+="y"
                s = s[3:]
            elif s[:3]=="26#":
                w+="z"
                s = s[3:]
        if len(s)>=1:
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
