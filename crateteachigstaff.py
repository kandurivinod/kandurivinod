import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
ctq="create table teaching_staff(uid int,name char(200),phone_number varchar(10), role char(20),school_id int)"
cur.execute(ctq)