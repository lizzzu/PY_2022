def fun(a, b):
    return (
        set(a).intersection(set(b)),
        set(a).union(set(b)),
        set(a).difference(set(b)),
        set(b).difference(set(a))
    )

print(fun([1, 2, 3, 4, 5], [4, 5, 6, 7]))
