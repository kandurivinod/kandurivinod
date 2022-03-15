import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database='nandyal')
cur=con.cursor()
ctq="create table student_marks(uid int,engils int,maths int,science int,physics int,chemistry int,hindi int,student_id int,type_of_exam char(20),class_id int,school_id int,grade char(10),percentage int,result_status char(10),tota_marks int)"
cur.execute(ctq)