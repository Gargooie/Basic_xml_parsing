import os
import psycopg2
import requests
from xml.etree import ElementTree


r = requests.get('https://api.ilsa.ru/sale/v1/dealers.xml?q=status:exchange')
#user = r.content
#user2 = r.text
#print(user2) 

courses = ElementTree.fromstring(r.content)
#for c in tree:
#	name = c.find('Name').text
#	print(name)
	
	
for c in courses:
	dealer_id = c.get('Id')
	name = c.find('Name').text
	brand = c.find('Brand').text
	print(dealer_id)
	print(name)
	print(brand)