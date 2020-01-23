import os
import psycopg2
import requests
from xml.etree import ElementTree
from lxml import etree
file_name = 'offers2.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)

root = dom.getroot()

tree = etree.parse('offers2.xml')
root = tree.getroot()
	





x=0

con = psycopg2.connect(
                                  user = "ilsa",
                                  password = "111",
                                  host = "192.168.10.107",
                                  port = "5432",
                                  database = "ilsa"
								  )


cur = con.cursor()
	
cur.execute('truncate table dealers_management.property_id')
cur.execute('truncate table dealers_management.vehicles')


token = '&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA'
link = 'http://api.ilsa.ru/auto/v1/offers?q=dealer%3ARU77KI02'
linkage = link + "&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA"

r2 = requests.get('https://api.ilsa.ru/auto/v1/offers?q=dealer%3ARU77KI02&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA')
print(linkage)

#courses = ElementTree.fromstring(r2.content)
courses = dom.findall('Vehicle')

for c in courses:
	x +=1
	dealer_id = x
	
	vehicle_id 			= c.get('Id')
	vin 				= c.find('VIN').text
	creation_date 		= c.find('CreationDate').text
	updated_date		= c.find('UpdateDate').text
	mark				= c.find('Mark').text
	model				= c.find('Model').text
	modification		= c.find('Modification').text
	modification_code	= c.find('ModificationCode').text
	modification_index	= c.find('ModificationIndex').text
	color				= c.find('Color').text
	price				= c.find('Price').text
	
	color_code			= "NULL"
	condition_id		= "NULL"
	condition_mileage	= "NULL"
	price_currency		= "NULL"
		
	
	#searching for nested attributes >>>>
	foobars = dom.findall('.//Condition')
	y=0
	for elem in foobars:
		y +=1
		if x == y:
			condition_id = elem.get('Id')
			condition_mileage = elem.get('Mileage')
			
	#<<<


	#searching for nested attributes >>>>
	
	y=0
	foobars2 = dom.findall('.//Color')
	for elem in foobars2:
		y +=1
		if x == y:
			color_code			= elem.get('Code')
	
	y = 0
	foobars3 = dom.findall('.//Price')
	for elem in foobars3:
		y +=1
		if x == y:
			price_currency		= elem.get('Currency')




	#print(' * {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
	#	vehicle_id, creation_date, updated_date, condition_id,condition_mileage, mark, model, modification, modification_code,modification_index,color_code, color, price_currency, price				
	#))
#Property grabbing >>>
	

	
	con.commit()
	cur.execute("insert into dealers_management.vehicles ( dealer_id, vin, vehicle_id , creation_date, updated_date, mark, model, modification, modification_code, modification_index, color, price, color_code, price_currency, condition_id, condition_mileage)"
	" values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (dealer_id, vin, vehicle_id , creation_date, updated_date, mark, model, modification, modification_code, modification_index, color, price, color_code, price_currency, condition_id, condition_mileage))


#con.commit()




def insert(a):
	property_text = root.xpath("//Property[contains(@Id,'" + a + "')]")
	property_id = a
	property_value = property_text[0].text
	#print(property_value)
	value = property_value
	if value is not None:
		cur.execute("insert into dealers_management.property_id (vehicle_id, property_id, value, creation_date, updated_date)"
		" values ( %s, %s, %s, %s, %s)", (vehicle_id, property_id, value, creation_date, updated_date))
	


property_count = []
props_array = dom.findall('.//Property')

for elem in props_array:
	property_unit = elem.get('Id')

	
	insert(property_unit)

con.commit()



cur.close()
