import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_details values(2,'pavani',1,9645782315,'sreenu',8574965415,'a',10)"
cur.execute(iq)
con.commit()