def how_many_1s(n):
    return bin(n)[2:].count('1')

print(how_many_1s(24))
