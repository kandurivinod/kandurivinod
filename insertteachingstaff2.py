import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into teaching_staff values(2,'krishna',8574963241,'teacher',1)"
cur.execute(iq)
con.commit()