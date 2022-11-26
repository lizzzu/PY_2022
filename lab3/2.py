def fun(string):
    d = {}
    for letter in string:
        d.setdefault(letter, string.count(letter))
    return d

print(fun('Ana are mere.'))
