def fun(*lists):
    lg = max(len(l) for l in lists)
    return [tuple(l[i] if i < len(l) else None for l in lists) for i in range(lg)]

print(fun([1, 2, 3], [5, 6, 7], ['a', 'b', 'c']))
print(fun([1, 2, 3], [5, 6, 7, 8, 9], ['a', 'b', 'c', 10]))
