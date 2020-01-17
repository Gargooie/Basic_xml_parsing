import os
import psycopg2
import urllib.request
from xml.etree import ElementTree
file_name = 'dealers.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)
#dom = ElementTree(file=urllib.request.urlopen('https://api.ilsa.ru/sale/v1/dealers.xml' % i ))

#print(dom)

#connection to the DB
con = psycopg2.connect(
                                  user = "ilsa",
                                  password = "111",
                                  host = "192.168.10.107",
                                  port = "5432",
                                  database = "ilsa"
								  )


cur = con.cursor()

#importing xml
courses = dom.findall('Dealer')
x=0
for c in courses:
	dealer_id = c.get('Id')
	name = c.find('Name').text
	brand = c.find('Brand').text
	#location = c.get('Location/Longitue')
	area = c.find('Location/Area').text
	region = c.find('Location/Region').text
	try:
		district = c.find('Location/District').text
	except AttributeError:
		pass
	#end of exception block  <<<
	#taking nested attributes >>>
	y=0
	foobars = dom.findall('.//Location')
	
	for elem in foobars:
		y +=1
		id2 = elem.get('Id')
		if x == y:
			longitude = elem.get('Longitude')
			latitude = elem.get('Latitude')
	# taking nested attributes <<<<

	address = c.find('Location/Address').text
	phone_number = c.find('PhoneNumber').text
	www = c.find('Www').text
	updated_date = c.find('Offers/UpdatedDate').text
	link = c.find('Offers/Link').text
	internal_extension_number = c.find('InternalExtensionNumber').text
	try:
		cur.execute("insert into dealers_management.dealers ( dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number)"
		" values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ( dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number))
	except:
		print(dealer_id, end=" ")
		print("уже существует в таблице")
	#Printing out the transmittable values
	#print("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",  dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number)
	con.commit()
	
	#vehicles upload @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@>>>
	
	""" connection to vehicles xml >>>
	linkage = link
	linkage = link + "&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA"
	connect2 = requests.get(linkage)
	tree2 = ElementTree.fromstring(connect2.content)
	courses3 = tree.findall('Vehicle')

	for c3 in courses3:

		vehicle_id 			= c3.get('Id')
		creation_date 		= c3.find('CreationDate').text
		updated_date		= c3.find('UpdateDate').text
		condition_id		= c3.find('Id').text		#get
		condition_mileage	= c3.find('Mileage').text			#get
		mark				= c3.find('Mark').text
		model				= c3.find('Model').text
		modification		= c3.find('Modification').text
		modification_code	= c3.find('ModificationCode').text
		modification_index	= c3.find('ModificationIndex').text
		color_code			= c3.find('Code').text
		color				= c3.find('Color').text
		price_currency		= c3.find('Currency').text
		price				= c3.find('Price').text
	"""		#connection to vehicles xml <<<
	#vehicles upload @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@<<<
#===================psycopg


#cur.execute("SELECT id, name, Brand, Location FROM test_19_12 
#WHERE brand = brand)

#rows = cur.fetchall()

#for x in rows:
#	print(f"id {x[0]} name {x[1]} {x[2]}")


#mySQLQuery = ("""
#	SELECT amhandler, amname FROM pg_am WHERE oid = '403'
#	""")

#cur.execute(mySQLQuery)



#result = cur.fetchall()
#print(result)


cur.close()


























