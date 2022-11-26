def fun(*pos, **keywords):
    return len([p for p in pos if p in keywords.values()])

print(fun(1, 2, 3, 4, x=1, y=2, z=3, w=5))
