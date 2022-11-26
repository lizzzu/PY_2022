string = input().lower()
vowels = 0
for vowel in 'aeiou':
    vowels += string.count(vowel)
print(vowels)
