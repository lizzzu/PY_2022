def fun(heights):
    smol = []
    for row in range(1, len(heights)):
        for col in range(1, len(heights[0])):
            if len([i for i in range(row) if heights[i][col] >= heights[row][col]]) > 0:
                smol += [(row, col)]
    return smol

print(fun(
    [[1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]]
))
