import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123")
cur=con.cursor()
dbc="create database nandyal "
cur.execute(dbc)