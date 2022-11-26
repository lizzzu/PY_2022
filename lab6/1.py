import re

def fun(text):
    return re.findall(r'\w+', text)

print(fun('Ana are ~3 mere si 120 +/-5 pere.'))
