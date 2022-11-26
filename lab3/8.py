def loop(mapping):
    list = []
    value = mapping['start']
    while value not in list:
        list += [value]
        value = mapping[value]
    return list

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
