def fun(words):
    dictionary = {}
    for word in words:
        dictionary[word[-2:]] = dictionary.get(word[-2:], []) + [word]
    return [[word for word in dictionary[i]] for i in dictionary] # list(dictionary.values())

print(fun(['ana', 'banana', 'carte', 'arme', 'parte']))
