def fun(pairs):
    pairs.sort(key=lambda pair: pair[1][2])
    return pairs

print(fun([('abc', 'bcd'), ('abc', 'zza')]))
