import psycopg2

#connect to the db
con = psycopg2.connect(
                                  #user = "dunaev",
                                  #password = "8826447",
                                  host = "192.168.10.126",
                                  port = "1433",
                                  #database = "ILSA"
								  )

#cursor
cur = con.cursor()

#execute query
cur.execute('select id, number from dbo.fedresurs')



rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} number {r[1]}")

#close the cursor
cur.close()
#close the connection
con.close()