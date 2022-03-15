import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Vinod@123",database="nandyal")
cur=con.cursor()
while(True):
    uid=int(input("uid:"))
    english=int(input("Enter english marks:"))
    maths=int(input("Enter maths marks:"))
    science=int(input("Enter science marks:"))
    physics=int(input("Enter physics marks:"))
    chemistry=int(input("Enter chemistry marks:"))
    hindi=int(input("Enter hindi marks:"))
    student_id=int(input("enter student_id:"))
    type_of_exam=input("enter type of exam:")
    class_id=int(input("enter class_id:"))
    school_id=int(input("Enter school_id:"))
    grade=input("enter the grade:")
    percentage=int(input("enter percentage:"))
    result_status=input("enter result_status:")
    total_marks=int(input("enter total_marks:"))
    diq="insert into student_marks values(%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,%d,'%s',%d,'%s',%d,)"
    cur.execute(diq %(uid,english,maths,science,physics,chemistry,hindi,student_id,type_of_exam,class_id,school_id,grade,percentage,result_status,total_marks))
    con.commit()
    print("{} row inserted dynamically into employee table:".format(cur.rowcount))
    ch=input("Do u want to insert another Record(yes/no):")
    if(ch=="no"):
        break
    if(ch!='yes'):
        print("Plz Learn typing :")
        break
