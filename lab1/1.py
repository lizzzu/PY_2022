import math

numbers = input().split()
gcd = int(numbers[0])
for number in numbers:
    gcd = math.gcd(gcd, int(number))
print(gcd)
