grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] #8

def countNegatives(grid):
    """
    import numpy
    return (sum(map(lambda i: 1 if i<0 else 0,(numpy.array(grid)).flatten())))
    """
    count = 0
    for i in range (len(grid)):
        for x in grid[i]:
            if x < 0:
                count+=1
    return count

print (countNegatives(grid))
