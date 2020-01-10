
import pyodbc



connection = pyodbc.connect('Driver=SQL Server;'
						'Server=sqlserver-dev;'
						#'Server=192.168.10.126;'
						#'Database=ILSA;'
						'Database=ILSA;'
						#'Uid=dunaev;'
						#'Pwd=8826447;'
						'Trusted_Connection=yes;'
						'Port=1433')
cursor = connection.cursor()

mySQLQuery = ("""
	select id, number from dbo.fedresurs WHERE number = '03421002'
	""")

cursor.execute(mySQLQuery)
results = cursor.fetchall()
print(results)

connection.close()