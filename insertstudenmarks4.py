import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_marks values(4,65,85,74,63,78,91,4,'half_yearly',10,1,'a',70,'pass',452)"
cur.execute(iq)
con.commit()