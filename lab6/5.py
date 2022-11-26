import xml.etree.ElementTree as et

def fun(path, attrs):
    return [elem for elem in et.parse(path).iter() if list(item for item in elem.attrib.items() if item in attrs.items())]

print(fun('./cd.xml', {
    'class': 'url',
    'name': 'url-form',
    'data-id': 'item'
}))
