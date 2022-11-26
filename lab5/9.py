from pprint import pprint

def fun(pairs):
    return [{'sum': x + y, 'prod': x * y, 'pow': x ** y} for x, y in pairs]

pprint(fun([(5, 2), (19, 1), (30, 6), (2, 2)]))
