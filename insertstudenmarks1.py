import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_marks values(1,58,79,56,43,57,99,1,'half_yearly',10,1,'b',60,'pass',369)"
cur.execute(iq)
con.commit()