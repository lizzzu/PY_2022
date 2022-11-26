def most_common_letter(s):
    letters = {}
    for c in s:
        if c.isalpha():
            if c in letters: letters[c] += 1
            else: letters[c] = 1
    return sorted(letters.items(), key=lambda l: l[1], reverse=True)[0]

print(most_common_letter('an apple is not a tomato'.lower()))
