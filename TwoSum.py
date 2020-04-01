from functools import reduce
nums = [2, 7, 11, 15]
target = 9
print(list(map(lambda a,b: a+b == target,nums)))
