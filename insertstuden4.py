import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
iq="insert into student_details values(4,'rafi',1,7485961452,'raju',6345789218,'a',10)"
cur.execute(iq)
con.commit()