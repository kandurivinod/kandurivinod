import mysql.connector  # step-1
def insertrecord():
	con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="school")
	cur=con.cursor()
	iq="insert into students values(13,'raju',8546789545,96,52,43,45,63,66,'sixth')"
	cur.execute(iq)
	con.commit()
	print("{} record inserted into students table:".format(cur.rowcount))


#main program
insertrecord()