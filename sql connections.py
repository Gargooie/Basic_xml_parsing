import pyodbc

connection = pyodbc.connect('Driver=SQL Server;'
						'Server=sqlserver-dev;'
						'Database=ImpExpRus;'
						'Trusted_Connection=yes;'
						#'Port=1433'
                        )
cursor = connection.cursor()

mySQLQuery = ("""
	SELECT  [TypeV] as t,[G011 (Направление перемещения)] as b,sum(convert(int,[G31_7 (кол-во товара в дополнительной единице измерения)])) as q
FROM [ImpExpRus].[dbo].[ImpExpTemp]
WHERE ([STAT(Признак учет в стат внешней торговли 1-учит 0-неучит)] IN ('1'))
AND (SUBSTRING([G33 (код товара по ТН ВЭД России)], 1, 4) IN ('8703', '8704', '8702') OR
                      SUBSTRING([G33 (код товара по ТН ВЭД России)], 1, 5) IN ('87012')) 
					  AND (TypeV in (1,2,3,4))  AND (ForUnload = 1)
group by [TypeV],[G011 (Направление перемещения)]

	""")

cursor.execute(mySQLQuery)
results = cursor.fetchall()
for row in cursor:
    print('name:', row.sum)    

counter=0
for x in results:
    counter +=1
   
   
y=0
arr=[0]*counter

myfile = open("file.txt", "w")

#loop for the source
for x in results:
    arr[y]=x
    y +=1
    
    print(y, end = " ")
    print(x)




y=0
arr2=[0]*counter

############check for similarity
for x in results:
    arr2[y]=x
    
    if arr[y] != arr2[y]:
        print("the table has changed")
    
    y +=1
    
    
    
    
    print(y, end = " ")
    print(x)


cursor.close()
connection.close()