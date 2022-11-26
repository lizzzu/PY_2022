# 1
def fun(*args, **kwargs):
    sum = 0
    for val in kwargs.values():
        sum += val
    return sum

print('[1]', fun(1, 2, c=3, d=4))

# 2
print('[2]', (lambda *args, **kwargs: sum(kwargs.values()))(1, 2, c=3, d=4))
