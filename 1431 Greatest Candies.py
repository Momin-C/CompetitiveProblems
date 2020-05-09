#PROBLEM 1431
#SOURCE: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
def kidsWithCandies(candies, extraCandies):
    lst = []
    for i in candies:
        if i+extraCandies >= max(candies):
            lst.append(True)
        else:
            lst.append(False)
    return lst
