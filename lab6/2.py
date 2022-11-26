import re

def fun(regex, text, x):
    return [word for word in re.findall(regex, text) if len(word) == x]

print(fun(r'~?\w+\.?', 'A.n.a. _nu_ are.: nici ~3 mere si.. nici ~431 pere...', 4))
