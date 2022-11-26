string = 'CamelCaseWord'
string = ''.join(['_' + l.lower() if l.isupper() else l for l in string]).lstrip('_')
print(string)
