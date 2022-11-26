A = ['firs', 'n_lt', 'oba_', 'htyp']

string = ''

srow = 0
erow = len(A)
scol = 0
ecol = len(A[0])

while srow < erow and scol < ecol:
    for j in range(scol, ecol):
        string += A[srow][j]
    srow += 1

    for i in range(srow, erow):
        string += A[i][ecol - 1]
    ecol -= 1

    if srow < erow:
        for j in range(ecol - 1, scol - 1, -1):
            string += A[erow - 1][j]
        erow -= 1

    if scol < ecol:
        for i in range(erow - 1, srow - 1, -1):
            string += A[i][scol]
        scol += 1

print(string)
