import os
from xml.etree import ElementTree
file_name = 'dealers2.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)
#print(dom)



courses = dom.findall('Dealer')

for c in courses:
	#print(c.text)
	#dealer = c.find('Dealer Id').text
	name = c.find('Name').text
	brand = c.find('Brand').text
	location = c.find('Location').text
	phone_number = c.find('PhoneNumber').text
	www = c.find('Www').text
	updated_date = c.find('Offers/UpdatedDate').text
	link = c.find('Offers/Link').text
	internal_extension_number = c.find('InternalExtensionNumber').text
	
	print(' * {}, {}, {}, {}, {}, {}, {}, {}'.format(
		name, brand, location, phone_number, www, updated_date, link, internal_extension_number
	))