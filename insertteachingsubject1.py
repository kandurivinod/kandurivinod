import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into teaching_subjects values(1,'english',2,1)"
cur.execute(iq)
con.commit()