import os
from xml.etree import ElementTree
file_name = 'dealers4.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
from xml.dom import minidom
#print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)
#print(dom)Dealer/


x=0
courses = dom.getroot()

#garbage
#for temp in courses.find('//Dealer/Location'):
#	location_longitude = temp.attrib.get('Longitude')
#	print(location_longitude)

#doc = minidom.parse('dealers3.xml')
#items = doc.getElementsByTagName('item')
#print('Item #2 attribute:')
#print(items[0].attributes['name'].value)
#
## all item attributes
#print('\nAll attributes:')
#for elem in items:
#    print(elem.attributes['name'].value)
#
## one specific item's data
#print('\nItem #2 data:')
#print(items[0].firstChild.data)
#print(items[0].childNodes[0].data)
#
## all items data
#print('\nAll item data:')
#for elem in items:
#    print(elem.firstChild.data)

#my stuff@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#doc = minidom.parse('dealers2.xml')
#items = doc.getElementsByTagName('Dealer')
#print('Item #2 attribute:')
#print(items[0].attributes['Id'].value)

# all item attributes
#print('\nAll attributes:')
#for elem in items:
#    print(elem.attributes['Id'].value)

# one specific item's data
#print('\nItem #2 data:')
#print(items[0].firstChild.data)
#print(items[0].childNodes[0].data)

# all items data
#print('\nAll item data:')
#for elem in items:
 #   print(elem.firstChild.data)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#foobars = dom.findall('Dealer/Location')
#for elem in foobars:
#    print(elem.get('Latitude'))

#ids = [f.attrib.get('Longitude') for f in dom.findall('.//Location')]
#print(ids)

#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
y = 0
for c in courses:
	id = c.get('Id')
	name = c.find('Name').text
	brand = c.find('Brand').text
	#location_longitude = c.find[@attrib='Longitude'].text
	#location_latitude = c.get('Latitude')
	location_longitude = 1
	y +=1

	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@start")
	foobars = dom.findall('.//Location')
	x = 0
	for elem in foobars:
		x +=1
		print("forward", end = " ")
		print(x)
		id2 = elem.get('Id')
		print("+++")
		print(id)
		print(id2)
		if x == y:
			print(elem.get('Longitude'))
			print(elem.get('Latitude'))
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

	area = c.find('Location/Area').text
	region = c.find('Location/Region').text
	district = c.find('Location/District').text
	address = c.find('Location/Address').text
	phone_number = c.find('PhoneNumber').text
	www = c.find('Www').text
	updated_date = c.find('Offers/UpdatedDate').text
	link = c.find('Offers/Link').text
	internal_extension_number = c.find('InternalExtensionNumber').text



	x +=1
	print(x)
	print('{} => {}'
	#print('{}=> {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'
	#, {}, {}'
	.format(
	x, location_longitude
	#id, name, brand,
	#location_longitude, location_latitude,
	#area, region, district, address, phone_number, www, updated_date, link, internal_extension_number
	))
