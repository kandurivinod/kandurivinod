import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
ctq="create table teaching_subjects(uid int,subjects char(200),staff_id int,school_id int)"
cur.execute(ctq)