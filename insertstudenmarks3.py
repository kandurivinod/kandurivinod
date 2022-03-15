import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_marks values(3,56,43,95,52,96,94,3,'half_yearly',10,1,'b',66,'pass',452)"
cur.execute(iq)
con.commit()