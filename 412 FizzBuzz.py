#PROBLEM 412
#SOURCE: https://leetcode.com/problems/fizz-buzz/
def fizzBuzz(n):
    #SOLUTION 1
    lst = []
    for i in range(1,n+1):
        if i%3 ==0 and i%5==0:
            lst.append("FizzBuzz")
        elif i%3==0:
            lst.append("Fizz")
        elif i%5==0:
            lst.append("Buzz")
        else:
            lst.append(str(i))

    #SOLUTION 2 USING LIST COMPREHENSIONS
    #lst = ["FizzBuzz" if (i%3==0 and i%5==0) else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,n+1)]
    return lst
print (fizzBuzz(15))
