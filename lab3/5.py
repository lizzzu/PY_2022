def validate_dict(s, d):
    for key in d:
        if key not in (k[0] for k in s):
            return False
    for rule in s:
        if rule[0] not in d: return False
        if not d[rule[0]].startswith(rule[1]): return False
        if rule[2] not in d[rule[0]][1:-1]: return False
        if not d[rule[0]].endswith(rule[3]): return False
    return True

print(validate_dict(s={('key1', '', 'inside', ''), ('key2', 'start', 'middle', 'winter')}, d={'key1': 'come inside, it\'s too cold out', 'key3': 'this is not valid'}))
print(validate_dict(s={('key1', '', 'inside', ''), ('key2', 'start', 'middle', 'winter')}, d={'key1': 'come inside, it\'s too cold out', 'key2': 'start the middle with some winter'}))
