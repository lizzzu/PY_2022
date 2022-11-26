def build_xml_element(tag, content, **elements):
    return '<{} {}>{}</{}>'.format(tag, ''.join('{}="{}" '.format(key, value) for key, value in elements.items())[:-1], content, tag)

print(build_xml_element('a', 'Hello there', href='http://python.org', _class='my-link', id='someid'))
