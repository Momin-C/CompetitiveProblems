def kidsWithCandies(candies, extraCandies):
    lst = []
    for i in candies:
        if i+extraCandies >= max(candies):
            lst.append(True)
        else:
            lst.append(False)
    return lst
