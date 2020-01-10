import os
from xml.etree import ElementTree
file_name = 'offers2.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)
#print(dom)



courses = dom.findall('Vehicle')

for c in courses:
	vehicle_id 			= c.get('Id')
	creation_date 		= c.find('CreationDate').text
	updated_date		= c.find('UpdateDate').text
	condition_id		= c.get('Id')		#get
	condition_mileage	= c.get('Mileage')		#
	mark				= c.find('Mark').text
	model				= c.find('Model').text
	modification		= c.find('Modification').text
	modification_code	= c.find('ModificationCode').text
	modification_index	= c.find('ModificationIndex').text
	color_code			= c.get('Code')
	color				= c.find('Color').text
	price_currency		= c.get('Currency')
	price				= c.find('Price Currency').text


	print(' * {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
		vehicle_id, creation_date, updated_date, condition_id,condition_mileage, mark, model, modification, modification_code,modification_index,color_code, color, price_currency,price				
	))
