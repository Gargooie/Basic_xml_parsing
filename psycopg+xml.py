import os
import psycopg2
#import urllib.request
from xml.etree import ElementTree
file_name = 'dealers.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)
#dom2 = ElementTree(file=urllib.request.urlopen('https://api.ilsa.ru/sale/v1/dealers.xml' % i ))

print(dom)

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

for c in courses:
	dealer_id = c.get('Id')
	name = c.find('Name').text
	brand = c.find('Brand').text
	#location = c.get('Location/Longitue')
	area = c.find('Location/Area').text
	region = c.find('Location/Region').text
	district = c.find('Location/District').text
	address = c.find('Location/Address').text
	phone_number = c.find('PhoneNumber').text
	www = c.find('Www').text
	updated_date = c.find('Offers/UpdatedDate').text
	link = c.find('Offers/Link').text
	internal_extension_number = c.find('InternalExtensionNumber').text
	
	#cur.execute("insert into test_19_12 ( dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number)"
	#" values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ( dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number))
	
	#print("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",  dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number)
	#con.commit()

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


