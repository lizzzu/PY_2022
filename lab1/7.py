from re import findall

def extract_first_number(s):
    return findall('[0-9]+', s)[0]

print(extract_first_number('ana99 are 123 mere'))
