import requests
from xml.etree import ElementTree

r = requests.get('https://api.ilsa.ru/sale/v1/dealers.xml?q=status:exchange')
#user = r.content
#user2 = r.text
#print(user2) 

tree = ElementTree.fromstring(r.content)
for c in tree:
	name = c.find('Name').text
	print(name)