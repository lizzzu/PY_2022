import xml.etree.ElementTree as et

def fun(path, attrs):
    return [elem for elem in et.parse(path).iter() if all(item in elem.attrib.items() for item in attrs.items())]

print(fun('./cd.xml', {
    'class': 'url',
    'name': 'url-form',
    'data-id': 'item'
}))
