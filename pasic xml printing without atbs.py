import xml.etree.ElementTree as ET
tree = ET.parse('dealers2.xml')
root = tree.getroot()
 
# все данные
print('all the data:')
 
for elem in root:
   for subelem in elem:
      print(subelem.text)
