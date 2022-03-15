import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_details values(1,'vinod',1,8574963214,'pavan',9645786345,'a',10)"
cur.execute(iq)
con.commit()