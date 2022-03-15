import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_marks values(2,55,96,78,54,63,89,2,'half_yearly',10,1,'b',65,'pass',447)"
cur.execute(iq)
con.commit()