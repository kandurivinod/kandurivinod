import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="pklr")
cur=con.cursor()
ct="create table student(stdno int, name char(20),phone_number varchar(10), address char(10))"
cur.execute(ct)





