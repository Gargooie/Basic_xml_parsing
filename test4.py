import os
import psycopg2

from xml.etree import ElementTree
from lxml import etree
file_name = 'offers2.xml'
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
	
	tree = etree.parse('offers.xml')
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
	


	property_id_1007 = root.xpath("//Property[contains(@Id,'1007')]")
	property_id_1022 = root.xpath("//Property[contains(@Id,'1022')]")
	property_id_1023 = root.xpath("//Property[contains(@Id,'1023')]")
	property_id_1101 = root.xpath("//Property[contains(@Id,'1101')]")
	property_id_1102 = root.xpath("//Property[contains(@Id,'1102')]")
	property_id_1103 = root.xpath("//Property[contains(@Id,'1103')]")
	property_id_1104 = root.xpath("//Property[contains(@Id,'1104')]")
	property_id_1105 = root.xpath("//Property[contains(@Id,'1105')]")
	property_id_1106 = root.xpath("//Property[contains(@Id,'1106')]")
	property_id_1107 = root.xpath("//Property[contains(@Id,'1107')]")
	property_id_1108 = root.xpath("//Property[contains(@Id,'1108')]")
	property_id_1201 = root.xpath("//Property[contains(@Id,'1201')]")
	property_id_1204 = root.xpath("//Property[contains(@Id,'1204')]")
	property_id_1222 = root.xpath("//Property[contains(@Id,'1222')]")
	property_id_1224 = root.xpath("//Property[contains(@Id,'1224')]")
	property_id_1226 = root.xpath("//Property[contains(@Id,'1226')]")
	property_id_1301 = root.xpath("//Property[contains(@Id,'1301')]")
	property_id_1401 = root.xpath("//Property[contains(@Id,'1401')]")
	
	property_id_2101 = root.xpath("//Property[contains(@Id,'2101')]")
	property_id_2102 = root.xpath("//Property[contains(@Id,'2102')]")
	property_id_2103 = root.xpath("//Property[contains(@Id,'2103')]")
	property_id_2201 = root.xpath("//Property[contains(@Id,'2201')]")
	property_id_2202 = root.xpath("//Property[contains(@Id,'2202')]")
	property_id_2203 = root.xpath("//Property[contains(@Id,'2203')]")
	property_id_2204 = root.xpath("//Property[contains(@Id,'2204')]")
	property_id_2301 = root.xpath("//Property[contains(@Id,'2301')]")
	property_id_2302 = root.xpath("//Property[contains(@Id,'2302')]")
	
	property_id_3101 = root.xpath("//Property[contains(@Id,'3101')]")
	property_id_3102 = root.xpath("//Property[contains(@Id,'3102')]")
	property_id_3103 = root.xpath("//Property[contains(@Id,'3103')]")
	property_id_3104 = root.xpath("//Property[contains(@Id,'3104')]")
	property_id_3201 = root.xpath("//Property[contains(@Id,'3201')]")
	property_id_3301 = root.xpath("//Property[contains(@Id,'3301')]")
	property_id_3401 = root.xpath("//Property[contains(@Id,'3401')]")
	property_id_3501 = root.xpath("//Property[contains(@Id,'3501')]")
	property_id_3601 = root.xpath("//Property[contains(@Id,'3601')]")
	
	property_id_4101 = root.xpath("//Property[contains(@Id,'4101')]")
	property_id_4102 = root.xpath("//Property[contains(@Id,'4102')]")
	property_id_4103 = root.xpath("//Property[contains(@Id,'4103')]")
	property_id_4104 = root.xpath("//Property[contains(@Id,'4104')]")
	property_id_4105 = root.xpath("//Property[contains(@Id,'4105')]")
	property_id_4106 = root.xpath("//Property[contains(@Id,'4106')]")
	property_id_4107 = root.xpath("//Property[contains(@Id,'4107')]")
	property_id_4108 = root.xpath("//Property[contains(@Id,'4108')]")
	property_id_4109 = root.xpath("//Property[contains(@Id,'4109')]")
	property_id_4110 = root.xpath("//Property[contains(@Id,'4110')]")
	property_id_4111 = root.xpath("//Property[contains(@Id,'4111')]")
	property_id_4112 = root.xpath("//Property[contains(@Id,'4112')]")
	property_id_4113 = root.xpath("//Property[contains(@Id,'4113')]")
	property_id_4114 = root.xpath("//Property[contains(@Id,'4114')]")
	property_id_4115 = root.xpath("//Property[contains(@Id,'4115')]")
	property_id_4116 = root.xpath("//Property[contains(@Id,'4116')]")
	property_id_4117 = root.xpath("//Property[contains(@Id,'4117')]")
	property_id_4118 = root.xpath("//Property[contains(@Id,'4118')]")
	property_id_4119 = root.xpath("//Property[contains(@Id,'4119')]")
	property_id_4120 = root.xpath("//Property[contains(@Id,'4120')]")
	property_id_4121 = root.xpath("//Property[contains(@Id,'4121')]")
	property_id_4122 = root.xpath("//Property[contains(@Id,'4122')]")
	property_id_4123 = root.xpath("//Property[contains(@Id,'4123')]")
	property_id_4124 = root.xpath("//Property[contains(@Id,'4124')]")
	property_id_4125 = root.xpath("//Property[contains(@Id,'4125')]")
	property_id_4126 = root.xpath("//Property[contains(@Id,'4126')]")
	property_id_4127 = root.xpath("//Property[contains(@Id,'4127')]")
	property_id_4201 = root.xpath("//Property[contains(@Id,'4201')]")
	property_id_4202 = root.xpath("//Property[contains(@Id,'4202')]")
	
	property_id_5101 = root.xpath("//Property[contains(@Id,'5101')]")
	property_id_5102 = root.xpath("//Property[contains(@Id,'5102')]")
	property_id_5201 = root.xpath("//Property[contains(@Id,'5201')]")
	property_id_5202 = root.xpath("//Property[contains(@Id,'5202')]")
	property_id_5203 = root.xpath("//Property[contains(@Id,'5203')]")
	property_id_5204 = root.xpath("//Property[contains(@Id,'5204')]")
	property_id_5205 = root.xpath("//Property[contains(@Id,'5205')]")
	property_id_5301 = root.xpath("//Property[contains(@Id,'5301')]")
	property_id_5302 = root.xpath("//Property[contains(@Id,'5302')]")
	property_id_5401 = root.xpath("//Property[contains(@Id,'5401')]")
	property_id_5402 = root.xpath("//Property[contains(@Id,'5402')]")
	property_id_5403 = root.xpath("//Property[contains(@Id,'5403')]")
	property_id_5404 = root.xpath("//Property[contains(@Id,'5404')]")
	property_id_5405 = root.xpath("//Property[contains(@Id,'5405')]")
	property_id_5406 = root.xpath("//Property[contains(@Id,'5406')]")
	property_id_5407 = root.xpath("//Property[contains(@Id,'5407')]")
	property_id_5408 = root.xpath("//Property[contains(@Id,'5408')]")
	property_id_5409 = root.xpath("//Property[contains(@Id,'5409')]")
	property_id_5410 = root.xpath("//Property[contains(@Id,'5410')]")
	property_id_5411 = root.xpath("//Property[contains(@Id,'5411')]")
	property_id_5412 = root.xpath("//Property[contains(@Id,'5412')]")
	property_id_5413 = root.xpath("//Property[contains(@Id,'5413')]")
	property_id_5414 = root.xpath("//Property[contains(@Id,'5414')]")
	property_id_5415 = root.xpath("//Property[contains(@Id,'5415')]")
	property_id_5416 = root.xpath("//Property[contains(@Id,'5416')]")
	property_id_5417 = root.xpath("//Property[contains(@Id,'5417')]")
	property_id_5418 = root.xpath("//Property[contains(@Id,'5418')]")
	property_id_5419 = root.xpath("//Property[contains(@Id,'5419')]")
	property_id_5420 = root.xpath("//Property[contains(@Id,'5420')]")
	property_id_5421 = root.xpath("//Property[contains(@Id,'5421')]")
	property_id_5422 = root.xpath("//Property[contains(@Id,'5422')]")
	property_id_5501 = root.xpath("//Property[contains(@Id,'5501')]")
	property_id_5502 = root.xpath("//Property[contains(@Id,'5502')]")
	property_id_5503 = root.xpath("//Property[contains(@Id,'5503')]")
	property_id_5504 = root.xpath("//Property[contains(@Id,'5504')]")
	property_id_5505 = root.xpath("//Property[contains(@Id,'5505')]")
	property_id_5506 = root.xpath("//Property[contains(@Id,'5506')]")
	
	property_id_6101 = root.xpath("//Property[contains(@Id,'6101')]")
	property_id_6102 = root.xpath("//Property[contains(@Id,'6102')]")
	property_id_6103 = root.xpath("//Property[contains(@Id,'6103')]")
	property_id_6104 = root.xpath("//Property[contains(@Id,'6104')]")
	property_id_6105 = root.xpath("//Property[contains(@Id,'6105')]")
	property_id_6106 = root.xpath("//Property[contains(@Id,'6106')]")
	property_id_6107 = root.xpath("//Property[contains(@Id,'6107')]")
	property_id_6108 = root.xpath("//Property[contains(@Id,'6108')]")
	property_id_6201 = root.xpath("//Property[contains(@Id,'6201')]")
	property_id_6202 = root.xpath("//Property[contains(@Id,'6202')]")
	property_id_6301 = root.xpath("//Property[contains(@Id,'6301')]")
	property_id_6401 = root.xpath("//Property[contains(@Id,'6401')]")
	property_id_6402 = root.xpath("//Property[contains(@Id,'6402')]")
	property_id_6501 = root.xpath("//Property[contains(@Id,'6501')]")
	property_id_6502 = root.xpath("//Property[contains(@Id,'6502')]")
	property_id_6503 = root.xpath("//Property[contains(@Id,'6503')]")
	property_id_6504 = root.xpath("//Property[contains(@Id,'6504')]")
	property_id_6601 = root.xpath("//Property[contains(@Id,'6601')]")
	property_id_6602 = root.xpath("//Property[contains(@Id,'6602')]")
	property_id_6603 = root.xpath("//Property[contains(@Id,'6603')]")
	property_id_6604 = root.xpath("//Property[contains(@Id,'6604')]")
	property_id_6605 = root.xpath("//Property[contains(@Id,'6605')]")
	property_id_6606 = root.xpath("//Property[contains(@Id,'6606')]")
	property_id_6701 = root.xpath("//Property[contains(@Id,'6701')]")
	property_id_6702 = root.xpath("//Property[contains(@Id,'6702')]")
	property_id_6703 = root.xpath("//Property[contains(@Id,'6703')]")
	property_id_6704 = root.xpath("//Property[contains(@Id,'6704')]")
	property_id_6705 = root.xpath("//Property[contains(@Id,'6705')]")
	property_id_6706 = root.xpath("//Property[contains(@Id,'6706')]")
	property_id_6707 = root.xpath("//Property[contains(@Id,'6707')]")
	property_id_6708 = root.xpath("//Property[contains(@Id,'6708')]")
	
	property_id_7101 = root.xpath("//Property[contains(@Id,'7101')]")
	
	
	
	
	def insert(a, b):
		property_id = a
		property_value = b[0].text
		value = property_value
		cur.execute("insert into dealers_management.property_id (vehicle_id, property_id, value, creation_date, updated_date)"
		" values ( %s, %s, %s, %s, %s)", (vehicle_id, property_id, value, creation_date, updated_date))
		
	
	insert("1007", property_id_1007)
	insert("1022", property_id_1022)
	insert("1023", property_id_1023)
	insert("1101", property_id_1101)
	insert("1102", property_id_1102)
	insert("1103", property_id_1103)	
	insert("1104", property_id_1104)
	insert("1105", property_id_1105)
	insert("1106", property_id_1106)
	insert("1107", property_id_1107)
	insert("1108", property_id_1108)
	insert("1201", property_id_1201)
	insert("1204", property_id_1204)
	insert("1222", property_id_1222)
	insert("1224", property_id_1224)
	insert("1226", property_id_1226)
	insert("1301", property_id_1301)
	insert("1401", property_id_1401)
	
	insert("2101", property_id_2101)
	insert("2102", property_id_2102)
	insert("2103", property_id_2103)
	insert("2201", property_id_2201)
	insert("2202", property_id_2202)
	insert("2203", property_id_2203)
	insert("2204", property_id_2204)
	insert("2301", property_id_2301)
	insert("2302", property_id_2302)
	
	insert("3101", property_id_3101)
	insert("3102", property_id_3102)
	insert("3103", property_id_3103)
	insert("3104", property_id_3104)
	insert("3201", property_id_3201)
	insert("3301", property_id_3301)
	insert("3401", property_id_3401)
	insert("3501", property_id_3501)
	insert("3601", property_id_3601)
	
	insert("4101", property_id_4101)
	insert("4102", property_id_4102)
	insert("4103", property_id_4103)
	insert("4104", property_id_4104)
	insert("4105", property_id_4105)
	insert("4106", property_id_4106)
	insert("4107", property_id_4107)
	insert("4108", property_id_4108)
	insert("4109", property_id_4109)
	insert("4110", property_id_4110)
	insert("4111", property_id_4111)
	insert("4112", property_id_4112)
	insert("4113", property_id_4113)
	insert("4114", property_id_4114)
	insert("4115", property_id_4115)
	insert("4116", property_id_4116)
	insert("4117", property_id_4117)
	insert("4118", property_id_4118)
	insert("4119", property_id_4119)
	insert("4120", property_id_4120)
	insert("4121", property_id_4121)
	insert("4122", property_id_4122)
	insert("4123", property_id_4123)
	insert("4124", property_id_4124)
	insert("4125", property_id_4125)
	insert("4126", property_id_4126)
	insert("4127", property_id_4127)
	insert("4201", property_id_4201)
	insert("4202", property_id_4202)
	
	insert("5101", property_id_5101)
	insert("5102", property_id_5102)
	insert("5201", property_id_5201)
	insert("5202", property_id_5202)
	insert("5203", property_id_5203)
	insert("5204", property_id_5204)
	insert("5205", property_id_5205)
	insert("5301", property_id_5301)
	insert("5302", property_id_5302)
	insert("5401", property_id_5401)
	insert("5402", property_id_5402)
	insert("5403", property_id_5403)
	insert("5404", property_id_5404)
	insert("5405", property_id_5405)
	insert("5406", property_id_5406)
	insert("5407", property_id_5407)
	insert("5408", property_id_5408)
	insert("5409", property_id_5409)
	insert("5410", property_id_5410)
	insert("5411", property_id_5411)
	insert("5412", property_id_5412)
	insert("5413", property_id_5413)
	insert("5414", property_id_5414)
	insert("5415", property_id_5415)
	insert("5416", property_id_5416)
	insert("5417", property_id_5417)
	insert("5418", property_id_5418)
	insert("5419", property_id_5419)
	insert("5420", property_id_5420)
	insert("5421", property_id_5421)
	insert("5422", property_id_5422)
	insert("5501", property_id_5501)
	insert("5502", property_id_5502)
	insert("5503", property_id_5503)
	insert("5504", property_id_5504)
	insert("5505", property_id_5505)
	insert("5506", property_id_5506)
	
	insert("6101", property_id_6101)
	insert("6102", property_id_6102)
	insert("6103", property_id_6103)
	insert("6104", property_id_6104)
	insert("6105", property_id_6105)
	insert("6106", property_id_6106)
	insert("6107", property_id_6107)
	insert("6108", property_id_6108)
	insert("6201", property_id_6201)
	insert("6202", property_id_6202)
	insert("6301", property_id_6301)
	insert("6401", property_id_6401)
	insert("6402", property_id_6402)
	insert("6501", property_id_6501)
	insert("6502", property_id_6502)
	insert("6503", property_id_6503)
	insert("6504", property_id_6504)
	insert("6601", property_id_6601)
	insert("6602", property_id_6602)
	insert("6603", property_id_6603)
	insert("6604", property_id_6604)
	insert("6605", property_id_6605)
	insert("6606", property_id_6606)
	insert("6701", property_id_6701)
	insert("6702", property_id_6702)
	insert("6703", property_id_6703)
	insert("6704", property_id_6704)
	insert("6705", property_id_6705)
	insert("6706", property_id_6706)
	insert("6707", property_id_6707)
	insert("6708", property_id_6708)
	
	insert("7101", property_id_7101)
		
	
	con.commit()
	"""
	print (property_id_1002[0].text)
	print (property_id_1007[0].text)               
	print (property_id_1022[0].text)               
	print (property_id_1023[0].text)
	print (property_id_1101[0].text)
	print (property_id_1102[0].text) 
	print (property_id_1103[0].text) 
	print (property_id_1104[0].text)
	print (property_id_1105[0].text)
	print (property_id_1106[0].text) 
	print (property_id_1107[0].text) 
	print (property_id_1108[0].text)
	print (property_id_1201[0].text)
	print (property_id_1204[0].text) 
	print (property_id_1222[0].text) 
	print (property_id_1224[0].text)
	print (property_id_1226[0].text)
	print (property_id_1301[0].text) 
	print (property_id_1401[0].text) 
"""
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
