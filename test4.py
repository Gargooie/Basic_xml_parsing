import requests
import os
from xml.etree import ElementTree

#import from a file
file_name = 'dealers2.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print("Файл: ", full_file) #full path to the file
dom = ElementTree.parse(full_file)


#import from url
r = requests.get('https://api.ilsa.ru/sale/v1/dealers.xml?q=status:exchange')
tree = ElementTree.fromstring(r.content)
courses2 = tree.findall('Dealer')

courses = dom.findall('Dealer')
#for c in courses:
x=0
token = '&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA'
linkage = '1'
for c in courses:

	id = c.get('Id')
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
	

	x +=1
	#print('{}=> {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
	#	x, id, name, brand, area, region, district, address, phone_number, www, updated_date, link, internal_extension_number
	
	#linkage = link
	#linkage = link
	#linkage.append("&t=autostat&access_token=ZWNiNzJjMjFkY2FmOWE5MDMwOWE3NDU1NzYwZDYyMGRlOWE4MGI4OTllMDYyYjU3ZTJiYmE3NmU4Yjc0NjU4MA")

		
	#))
	#connection to other api
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
		                 
	#property_group 1000
		property_id_1002 	= c3.find('1002')
		property_id_1007	= c3.find('').text
        property_id_1022	= c3.find('').text
		property_id_1023	= c3.find('').text
        property_id_1101	= c3.find('').text
		property_id_1102	= c3.find('').text
		property_id_1103	= c3.find('').text
		property_id_1104	= c3.find('').text
		property_id_1105	= c3.find('').text
		property_id_1106	= c3.find('').text
		property_id_1107	= c3.find('').text
		property_id_1108	= c3.find('').text
		property_id_1201	= c3.find('').text
		property_id_1204	= c3.find('').text
		property_id_1222	= c3.find('').text
		property_id_1224	= c3.find('').text
		property_id_1226	= c3.find('').text
		property_id_1301	= c3.find('').text
		property_id_1401	= c3.find('').text
		                  
		#PropertyGroup Id="2= 000"
		Property_Id_2101	= c3.find('').text
		Property_Id_2102	= c3.find('').text
		Property_Id_2103	= c3.find('').text
		Property_Id_2201	= c3.find('').text
		Property_Id_2202	= c3.find('').text
		Property_Id_2203	= c3.find('').text
		Property_Id_2204	= c3.find('').text
		Property_Id_2301	= c3.find('').text
		Property_Id_2302	= c3.find('').text
                         
		#Propert_yG_roup Id== "3000"
		Property_Id_3101	= c3.find('').text
		Property_Id_3102	= c3.find('').text
		Property_Id_3103	= c3.find('').text
		Property_Id_3104	= c3.find('').text
		Property_Id_3201	= c3.find('').text
		Property_Id_3301	= c3.find('').text
		Property_Id_3401	= c3.find('').text
		Property_Id_3501	= c3.find('').text
		Property Id_3601	= c3.find('').text
                          
		#PropertyGr_p Id="40= 00"
		Property_Id_4101	= c3.find('').text
		Property_Id_4102	= c3.find('').text
		Property_Id_4103	= c3.find('').text
		Property_Id_4104	= c3.find('').text
		Property_Id_4105	= c3.find('').text
		Property_Id_4106	= c3.find('').text
		Property_Id_4107	= c3.find('').text
		Property_Id_4108	= c3.find('').text
		Property_Id_4109	= c3.find('').text
		Property_Id_4110	= c3.find('').text
		Property_Id_4111	= c3.find('').text
		Property_Id_4112	= c3.find('').text
		Property_Id_4113	= c3.find('').text
		Property_Id_4114	= c3.find('').text
		Property_Id_4115	= c3.find('').text
		Property_Id_4116	= c3.find('').text
		Property_Id_4117	= c3.find('').text
		Property_Id_4118	= c3.find('').text
		Property_Id_4119	= c3.find('').text
		Property_Id_4120	= c3.find('').text
		Property_Id_4121	= c3.find('').text
		Property_Id_4122	= c3.find('').text
		Property_Id_4123	= c3.find('').text
		Property_Id_4124	= c3.find('').text
		Property_Id_4125	= c3.find('').text
		Property_Id_4126	= c3.find('').text
		Property_Id_4127	= c3.find('').text
		Property_Id_4201	= c3.find('').text
		Property_Id_4202	= c3.find('').text
                             
		#Propert_yG_roup Id== 5000
		Property_Id_5101	= c3.find('').text
		Property_Id_5102	= c3.find('').text
		Property_Id_5201	= c3.find('').text
		Property_Id_5202	= c3.find('').text
		Property_Id_5203	= c3.find('').text
		Property_Id_5204	= c3.find('').text
		Property_Id_5205	= c3.find('').text
		Property_Id_5301	= c3.find('').text
		Property_Id_5302	= c3.find('').text
		Property_Id_5401	= c3.find('').text
		Property_Id_5402	= c3.find('').text
		Property_Id_5403	= c3.find('').text
		Property_Id_5404	= c3.find('').text
		Property_Id_5405	= c3.find('').text
		Property_Id_5406	= c3.find('').text
		Property_Id_5407	= c3.find('').text
		Property_Id_5408	= c3.find('').text
		Property_Id_5409	= c3.find('').text
		Property_Id_5410	= c3.find('').text
		Property_Id_5411	= c3.find('').text
		Property_Id_5412	= c3.find('').text
		Property_Id_5413	= c3.find('').text
		Property_Id_5414	= c3.find('').text
		Property_Id_5415	= c3.find('').text
		Property_Id_5416	= c3.find('').text
		Property_Id_5417	= c3.find('').text
		Property_Id_5418	= c3.find('').text
		Property_Id_5419	= c3.find('').text
		Property_Id_5420	= c3.find('').text
		Property_Id_5421	= c3.find('').text
		Property_Id_5422	= c3.find('').text
		Property_Id_5501	= c3.find('').text
		Property_Id_5502	= c3.find('').text
		Property_Id_5503	= c3.find('').text
		Property_Id_5504	= c3.find('').text
		Property_Id_5505	= c3.find('').text
		Property_Id_5506	= c3.find('').text
                _  _          
		#Propert_Gr_p Id=6000 
		Property_Id_6101	= c3.find('').text
		Property_Id_6102	= c3.find('').text
		Property_Id_6103	= c3.find('').text
		Property_Id_6104	= c3.find('').text
		Property_Id_6105	= c3.find('').text
		Property_Id_6106	= c3.find('').text
		Property_Id_6107	= c3.find('').text
		Property_Id_6108	= c3.find('').text
		Property_Id_6201	= c3.find('').text
		Property_Id_6202	= c3.find('').text
		Property_Id_6301	= c3.find('').text
		Property_Id_6401	= c3.find('').text
		Property_Id_6402	= c3.find('').text
		Property_Id_6501	= c3.find('').text
		Property_Id_6502	= c3.find('').text
		Property_Id_6503	= c3.find('').text
		Property_Id_6504	= c3.find('').text
		Property_Id_6601	= c3.find('').text
		Property_Id_6602	= c3.find('').text
		Property_Id_6603	= c3.find('').text
		Property_Id_6604	= c3.find('').text
		Property_Id_6605	= c3.find('').text
		Property_Id_6606	= c3.find('').text
		Property_Id_6701	= c3.find('').text
		Property_Id_6702	= c3.find('').text
		Property_Id_6703	= c3.find('').text
		Property_Id_6704	= c3.find('').text
		Property_Id_6705	= c3.find('').text
		Property_Id_6706	= c3.find('').text
		Property_Id_6707	= c3.find('').text
		Property_Id_6708	= c3.find('').text
                              
		Property_Id_7101	= c3.find('').text