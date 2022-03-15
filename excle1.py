import mysql.connector
import xlrd
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="pklr")
cur=con.cursor()
loc=("C:\\Users\\vinod\\Desktop\\student.xlsx")
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,11):
    print(sheet.row_values(i))
con.close()