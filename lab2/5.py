def modified_matrix(M):
    return [[M[i][j] if i != j else 0 for j in range(len(M))] for i in range(len(M[0]))]

print(modified_matrix(
    [[1, 2, 3, 2],
    [2, 4, 4, 3],
    [5, 5, 2, 5],
    [6, 6, 7, 6]]
))
