def fun(a):
    return list(zip([i for i in a if i % 2 == 0], [i for i in a if i % 2 == 1]))

print(fun([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
