import os
import psycopg2
import urllib.request
import requests
from xml.etree import ElementTree
from lxml import etree
file_name = 'dealers2.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)
#dom = ElementTree(file=urllib.request.urlopen('https://api.ilsa.ru/sale/v1/dealers.xml' % i ))

r = requests.get('https://api.ilsa.ru/sale/v1/dealers.xml?q=status:exchange')
#user = r.content
#user2 = r.text
#print(user2) 


#delete it!!!
root = dom.getroot()

tree = etree.parse('offers.xml')
root = tree.getroot()
#


#connection to the DB
con = psycopg2.connect(
                                  user = "ilsa",
                                  password = "111",
                                  host = "192.168.10.107",
                                  port = "5432",
                                  database = "ilsa"
								  )


cur = con.cursor()

cur.execute('truncate table dealers_management.dealers')
cur.execute('truncate table dealers_management.property_id')
cur.execute('truncate table dealers_management.vehicles')


#importing xml
#courses = ElementTree.fromstring(r.content)
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
    x +=1
    y=0
    foobars = dom.findall('.//Location')

    for elem in foobars:
        y +=1
        id2 = elem.get('Id')
        if x == y:
            longitude = elem.get('Longitude')
            latitude = elem.get('Latitude')
            region_id = elem.get('Id')

    foobars = dom.findall('.//Region')
    y=0
    for elem in foobars:
        y +=1
        if x == y:
            region_id = elem.get('Id')

    # taking nested attributes <<<<

    address = c.find('Location/Address').text
    phone_number = c.find('PhoneNumber').text
    www = c.find('Www').text
    updated_date = c.find('Offers/UpdatedDate').text
    link = c.find('Offers/Link').text
    internal_extension_number = c.find('InternalExtensionNumber').text
    try:
        cur.execute("insert into dealers_management.dealers ( dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number, location_longitude, location_latitude, region_id)"
        " values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ( dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number, longitude, latitude, region_id))
    except:
        print(dealer_id, end=" ")
        print("уже существует в таблице")
    #Printing out the transmittable values
    #print("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",  dealer_id, name , brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number)
    con.commit()

#vehicles upload @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@>>>
    token = '&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA'
    link = 'http://api.ilsa.ru/auto/v1/offers?q=dealer%3ARU77KI02'
    linkage = link + "&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA"
    r2 = requests.get('https://api.ilsa.ru/auto/v1/offers?q=dealer%3ARU77KI02&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA')


    #r2 = requests.get(linkage)
    print(linkage)

    #courses = ElementTree.fromstring(r2.content)
    #courses = courses.findall('Vehicle')




    courses2 = dom2.findall('Vehicle')
    

    for c in courses2:
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


























