import re

def fun(text):
    words = text.split(' ')
    for w, word in enumerate(words):
        if re.match(r'\w+', word):
            if word[0].lower() in 'aeiou' and word[-1].lower() in 'aeiou':
                for i in range(1, len(word), 2):
                    word = word[:i] + '*' + word[i + 1:]
                words[w] = word
        if re.match(r'\w+\W{1}', word):
            if word[0].lower() in 'aeiou' and word[-2].lower() in 'aeiou':
                for i in range(1, len(word) - 1, 2):
                    word = word[:i] + '*' + word[i + 1:]
                words[w] = word
    return ' '.join(words)

print(fun('Ana are  amere,   pere si  ananasi.'))
