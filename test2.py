import xml.dom.minidom

def main():

	doc =  xml.dom.minidom.parse("dealers.xml");
	print (doc.nodeName)
	print (doc.firstChild.tagName)
	
#	zAppointments = doc.getElementsByTagName("zAppointments")
#	print("%d expertise:" % zAppointments.length)
#	for skill in zAppointments:
#		print(skill.getAttribute("reminder"))
	expertise = doc.getElementsByTagName("Dealer")
	print("%d Dealer:" % expertise.length)
	for skill in expertise:
		print (skill.getAttribute("Id"))

	
if __name__ == "__main__":
	main();