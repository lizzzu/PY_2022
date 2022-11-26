def fun(x=1, strings=[], flag=True):
    chars = []
    for string in strings:
        chars += [[char for char in string if ord(char) % x != flag]]
    return chars

print(fun(2, ['test', 'hello', 'lab002'], False))
