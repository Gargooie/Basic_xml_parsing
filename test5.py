import  csv
import xml.etree.cElementTree as ET
tree = ET.parse('Dealers.xml')
root = tree.getroot()
xml_data_to_csv =open('Out.csv','w')
list_head=[]
Csv_writer=csv.writer(xml_data_to_csv)
count=0
for element in root.findall('Dealer'):
    List_nodes =[]

    #Get head by tag
    if count == 0:
       name = element.find('Name').tag
       list_head.append(name)

       brand = element.find('Brand').tag
       list_head.append(brand)

       www = element.find('Www').tag
       list_head.append(www)
       Csv_writer.writerow(list_head)
       count = +1

    #get child node
    name = element.find('Name').text
    List_nodes .append(name)

    brand = element.find('Brand').text
    List_nodes.append(brand)

    www = element.find('Www').text
    List_nodes.append(www)

    #Write List_nodes to csv
    Csv_writer.writerow(List_nodes)
xml_data_to_csv.close()