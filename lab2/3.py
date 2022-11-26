def lists_op(a, b):
    return (
        [el for el in a if el in b],
        [el for el in a if el not in b] + [el for el in b],
        [el for el in a if el not in b],
        [el for el in b if el not in a]
    )

print(lists_op([1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9, 10]))
