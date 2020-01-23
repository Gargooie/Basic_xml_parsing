import os
import psycopg2
import urllib.request
import requests
from xml.etree import ElementTree
from lxml import etree
file_name = 'offers2.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)

root = dom.getroot()

tree = etree.parse('offers.xml')
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

r = requests.get('https://api.ilsa.ru/auto/v1/offers?q=dealer%3ARU77KI02&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA')
print(linkage)

courses = ElementTree.fromstring(r.content)
#courses = dom.findall('Vehicle')

for c in courses:
    x +=1
    dealer_id = x

    vehicle_id 			= c.get('Id')   
    print(vehicle_id)

    vin 				= c.find('VIN').text

    #creation_date 		= c.find('CreationDate').text
    #updated_date		= c.find('UpdateDate').text
    #mark				= c.find('Mark').text
    #model				= c.find('Model').text
    #modification		= c.find('Modification').text
    #modification_code	= c.find('ModificationCode').text
    #modification_index	= c.find('ModificationIndex').text
    #color				= c.find('Color').text
    #price				= c.find('Price').text

	
    
    
    
    
    
    
    
    
    
    
    
	

con.commit()



cur.close()
