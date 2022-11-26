def fun(list):
    return (
        len([i for i in list if list.count(i) == 1]),
        len(set([i for i in list if list.count(i) > 1]))
    )

print(fun([1, 2, 2, 3, 4, 5, 5, 5, 6]))
