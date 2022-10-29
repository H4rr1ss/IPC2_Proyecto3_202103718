import xml.etree.ElementTree as ET

tree = ET.parse('./IGNORAR/hola.xml')
root = tree.getroot()

for products in root.findall('product'):
    item = products.find('item')

    item_id = item.get('currency')

    print(item_id)

    if item_id == '$2':
        root.remove(products)

h = 'hola'
pepe = 'zw'


new = ET.SubElement(root, 'cliente')
ET.SubElement(new, '{}'.format(h),nit='nit').text='{}'.format(pepe)
ET.SubElement(new, 'address').text='textAddress'

print(root.tag)
tree.write('./IGNORAR/hola.xml', xml_declaration=True)