def palindrom(list):
    palindromes = [n for n in list if str(n) == str(n)[::-1]]
    return (palindromes, max(palindromes))

print(palindrom([1, 10, 101, 98203, 1983, 90909]))
