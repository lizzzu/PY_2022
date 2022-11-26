import re

def fun(text, regexes):
    words = set()
    for regex in regexes:
        for word in re.findall(regex, text):
            words.add(word)
    return list(words)

print(fun('Ana are ~3 mere si doua (2) pere...', [r'\w{4}\.?', '\d', r'\w[e]\w[e]']))
