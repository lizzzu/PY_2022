def process(**keywords):
    fib = [0, 1]
    for i in range(2, 1000):
        fib += [fib[i - 1] + fib[i - 2]]
    if 'filters' in keywords:
        for filter in keywords['filters']:
            fib = [n for n in fib if filter(n)]
    if 'offset' in keywords:
        fib = fib[keywords['offset']:]
    if 'limit' in keywords:
        fib = fib[:keywords['limit']]
    return fib

def sum_digits(x):
    return sum(map(int, str(x)))

print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
))
