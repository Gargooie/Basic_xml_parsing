import os
import psycopg2

from xml.etree import ElementTree
from lxml import etree
file_name = 'offers4.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)
#print(dom)



courses = dom.findall('Vehicle')
x=0

con = psycopg2.connect(
                                  user = "ilsa",
                                  password = "111",
                                  host = "192.168.10.107",
                                  port = "5432",
                                  database = "ilsa"
								  )


cur = con.cursor()
	


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
	"""		Presentation block<<<<
	print(vehicle_id 	)		
	print(creation_date )		
	print(updated_date	)	
	print(mark			)	
	print(model			)	
	print(modification	)	
	print(modification_code)	
	print(modification_index	)
	print(color				)
	print(price				)
	print(color_code				)
	print(price_currency				)
	print(condition_id				)
	print(condition_mileage				)
	"""	#	Presentation block<<<
	#<<<
	
	
	



	#print(' * {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
	#	vehicle_id, creation_date, updated_date, condition_id,condition_mileage, mark, model, modification, modification_code,modification_index,color_code, color, price_currency, price				
	#))
#Property grabbing >>>
	

	root = dom.getroot()
	
	tree = etree.parse('offers4.xml')
	root = tree.getroot()
	
	#list = list(filter(lambda x: '1002' in x.get('Id'), root.findall(".//Property[@Id]")))
	
	
	
	"""
	
	property_id = "1002"
	property_id_1002 = root.xpath("//Property[contains(@Id,'1002')]")
	property_value = property_id_1002[0].text
	value = property_value
	
	cur.execute("insert into dealers_management.property_id (vehicle_id, property_id, value)"
	" values ( %s, %s, %s)", (vehicle_id, property_id, value ))
	con.commit()

	"""
	



	
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
		
		
		
		
	#for prnt in property_count:
	#	print(prnt)
	
	
	"""
	def thousands():
		property_text = root.xpath("//Property[contains(@Id,'" + a + "')]")
		property_value = property_text[0].text
		print(property_value)
		value = property_value
		
		if value is not None:
			property_count +=property_id
			print("property_id")
	"""	
	
		
		


		
	

	
	con.commit()
	cur.execute("insert into dealers_management.vehicles ( dealer_id, vin, vehicle_id , creation_date, updated_date, mark, model, modification, modification_code, modification_index, color, price, color_code, price_currency, condition_id, condition_mileage)"
	" values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (dealer_id, vin, vehicle_id , creation_date, updated_date, mark, model, modification, modification_code, modification_index, color, price, color_code, price_currency, condition_id, condition_mileage))

	
	#cur.execute("insert into dealers_management.property_id (vehicle_id, property_id, value)"
	#" values ( %s, %s, %s)", (vehicle_id, property_id, value ))
	#con.commit()
con.commit()
cur.close()




#print(list2[0].text)


"""

root = dom.getroot()
list = list(filter(lambda x: '1002' in x.get('Id'), root.findall(".//Property[@Id]")))
print(list[0].text)

foobars = dom.findall('Vehicle')
y=0
for elem in foobars:
	#property_group 1000
	property_id_1002 	= elem.find('Properties/PropertyGroup/Property').text
	print("GGGGGGGGGGGGGGGGG")
	print(property_id_1002)
	print("GGGGGGGGGGGGGGGGG")
	property_id_1007 	= elem.find('Properties/PropertyGroup/Property').text
	print(property_id_1007)
"""
	#property_id_1007	= elem.find('Id').text
	#property_id_1022	= elem.find('Id').textf
	#property_id_1023	= elem.find('Id').text
	#property_id_1101	= elem.find('Id').text
	#property_id_1102	= elem.find('Id').text
	#property_id_1103	= elem.find('Id').text
	#property_id_1104	= elem.find('Id').text
	#property_id_1105	= elem.find('Id').text
	#property_id_1106	= elem.find('Id').text
	#property_id_1107	= elem.find('Id').text
	#property_id_1108	= elem.find('Id').text
	#property_id_1201	= elem.find('Id').text
	#property_id_1204	= elem.find('Id').text
	#property_id_1222	= elem.find('Id').text
	#property_id_1224	= elem.find('Id').text
	#property_id_1226	= elem.find('Id').text
	#property_id_1301	= elem.find('Id').text
	#property_id_1401	= elem.find('Id').text

#first try
#root = dom.getroot()
#list = list(filter(lambda x: '1002' in x.get('Id'), root.findall(".//Property[@Id]")))
#print(list[0].text)
#lxml try

#for c in list:
#	x +=1
#	vehicle_id 			= c.get('Id')
	#vehicle_id2 			= c.find('Id').text
	#print(vehicle_id)



#print (list2[0].text)




"""
for elem in list:
		property_id_1007	= elem.find('').text
		print("GGGGGGGGGGGGGGGGG")
		print(property_id_1007)
		print("GGGGGGGGGGGGGGGGG")
"""
