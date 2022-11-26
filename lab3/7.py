from pprint import pprint

def fun(*sets):
    dict = {}
    for a in sets:
        for b in sets:
            if a != b:
                for op in '|&-':
                    dict['{} {} {}'.format(a, op, b)] = eval('{}{}{}'.format(a, op, b))
    return dict

pprint(fun({1, 2}, {2, 3}))
