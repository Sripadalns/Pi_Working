import MySQLdb

myDB = MySQLdb.connect(host="159.89.170.250",port=3306,user="root",passwd="sripals$38205_$",db="traccar")
cHandler = myDB.cursor()
cHandler.execute("SHOW DATABASES")
results = cHandler.fetchall()
for items in results:
    print items[0]
