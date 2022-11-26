def fibonacci(n):
    fib = [1, 1]
    i = 2
    while i < n:
        fib += [fib[i - 1] + fib[i - 2]]
        i += 1
    return fib[:n]

print(fibonacci(10))
