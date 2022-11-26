text = 'Programming in Python is fun'

# 1
def fun(string):
    vowels = []
    for char in string:
        if char.lower() in 'aeiou':
            vowels += [char]
    return vowels

print('[1]', fun(text))

# 2
import re
print('[2]', (lambda string: re.findall('[aeiou]', string))(text))

# 3
print('[3]', [char for char in text if char.lower() in 'aeiou'])
