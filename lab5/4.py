def fun(*args, **keywords):
    dictionaries = []
    for arg in args:
        if isinstance(arg, dict): dictionaries += [arg]
    for val in keywords.values(): dictionaries += [val]
    return [d for d in dictionaries if len(d) >= 2 and len([key for key in d if isinstance(key, str) and len(key) >= 3])]

print(fun(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True})
)
