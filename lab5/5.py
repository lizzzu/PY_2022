def fun(a):
    return [i for i in a if isinstance(i, int) or isinstance(i, float)]

print(fun([1, '2', {'3': 'a'}, {4, 5}, 5, 6, 3.0]))
