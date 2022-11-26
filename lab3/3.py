def fun(a, b):
    for key in a:
        if key not in b: return False
        elif type(a[key]) != type(b[key]): return False
        elif isinstance(a[key], dict) and isinstance(b[key], dict): return fun(a[key], b[key])
        elif a[key] != b[key]: return False
    for key in b:
        if key not in a: return False
    return True

print(fun(a={'a': 1, 'b': 2, 'c': {'d': 2}, 'f': 4, 'g': {'h': 8}}, b={'a': 2, 'b': 2, 'c': {'d': 3}, 'e': 4, 'g': 8}))
print(fun(a={'a': 1, 'b': 2, 'c': {'d': 2}}, b={'a': 1, 'b': 2, 'c': {'d': 2}}))
