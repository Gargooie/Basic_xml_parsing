
import pyodbc



cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.10.107;DATABASE=ILSA;UID=ilsa;PWD=111')
cursor = cnxn.cursor()
