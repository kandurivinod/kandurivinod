import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
In="select * from teaching_staff s left outer join teaching_subjects t on s.uid=t.uid"
cur.execute(In)