import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_details values(3,'mounika',1,8474125362,'teja',6574896154,'a',10)"
cur.execute(iq)
con.commit()