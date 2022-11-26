import math

def primes(list):
    return [el for el in list if len([i for i in range(2, int(math.sqrt(el)) + 1) if el % i == 0]) == 0]

print(primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
