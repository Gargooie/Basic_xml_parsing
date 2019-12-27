import psycopg2



#connect to the db
con = psycopg2.connect(
    user = "ilsa",
    password = "111",
    host = "192.168.10.107",
    port = "5432",
    database = "postgres")

#cursor
cur = con.cursor()

#execute query
cur.execute("select id, number from ILSA.dbo.fedresurs")



rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} number {r[1]}")

#close the cursor
cur.close()
#close the connection
con.close()