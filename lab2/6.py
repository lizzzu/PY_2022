def fun(*lists, x):
    items = {}
    for list in lists:
        for el in list:
            items[el] = items.get(el, 0) + 1
    return [el for el in items if items[el] == x]

print(fun([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, 'test'], x=2))
