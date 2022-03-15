import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="schools")
con.cursor()
iq="intsert into school_details  valuse(2,"kurnool public school","kurnool.in",8546321458,"Teja","kurnool",4)"
cur.execute(iq)
con.commit()