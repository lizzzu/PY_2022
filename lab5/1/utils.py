import math

def prime(n):
    if n & 1 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def process_item(x):
    if x <= 1: return 2
    while 1:
        x += 1
        if prime(x): return x
