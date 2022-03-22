#!/usr/bin/env python
# coding: utf-8

# In[2]:


def addop():
    a=int(input("enter a first  number:"))
    b=int(input("enter a second number:"))
    c=a+b
    print(c)
addop()


# In[3]:


def addop(a,b):
    c=a+b
    return c
a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
res=addop(a,b)
print(res)


# In[9]:


#There are 4 types are actual arguments are allowed in Python.
#1. positional arguments
#2. keyword arguments
#3. default arguments
#4. Variable length arguments
#1. positional arguments
#These are the arguments passed to function in correct positional order.
def dispstudinfo(sno,sname,marks):
    print("{}\t{}\t{}\t".format(sno,sname,marks))
print("stno\tsname\tmarks")
dispstudinfo(1,'vinod',78.66)
dispstudinfo(2,'balu',85.23)
dispstudinfo(3,'vasavi',95.23)
dispstudinfo(4,'mounika',74.23)
dispstudinfo(5,'teja',75.23)


# In[ ]:





# In[20]:


#default arguments
def disstudinfo(sno,sname,marks,school="zphp school"):
    print("{}\t{}\t{}\t{}".format(sno,sname,marks,school))
print("sno\tsname\tmarks\tschool")
disstudinfo(1,'mali',63.48)
disstudinfo(2,'balaji',65.48)
disstudinfo(3,'kumar',63.48,'ushodaya')
disstudinfo(4,'mani',83.48)


# In[3]:


def emp(eno,ename,esal):
    print("{}\t{}\t{}".format(eno,ename,esal))
print("eno\tename\tesal")
emp(1,'veeran',50000)
emp(ename='vinod',esal=80000,eno=2)
emp(esal=90000,eno=3,ename='vasavi')
emp(eno=4,esal=42000,ename='kumari')


# In[7]:


def disp(a):
    print(a)
def disp(a,b):
    print(a,b)
def disp(a,b,c):
    print(a,b,c)
disp(10)
disp(10,20)
disp(10,20,30)


# In[9]:


def disp(a):
    print(a)
disp(10)

def disp(a,b):
    print(a,b)
disp(10,20)

def disp(a,b,c):
    print(10,20,30)
disp(10,20,30)


# In[11]:


#varable length argument
def disp(*k):
    for val in k:
        print("{}".format(val),end=' ')
    print()

disp(10)
disp(10,20)
disp(10,20,30)
disp(10,20,30,40)


# In[12]:


#key word variable length argument
def  studhobbies( **k  ):
    print("------------------------")
    for key,val in k.items():
        print("\t{}-->{}".format(key,val))

#main program
studhobbies(stno=10,name="Off-Pavan",habit1="Eat Chewing Gum")
studhobbies(sno=20,sname="Rossum",Invent1="python2.x",invent2="Python3.x")
studhobbies(no=20,sname="Kiran",habit="Sleep")
studhobbies(sname="KVR",habit="Teaching")


# In[19]:


def studentinfo(**k):
    print("--------------------")
    for v,n in k.items():
        print("{}---->{}".format(v,n))
print("student information")
studentinfo(stno=1,sname='vinod',sectino='a',adders='hyd')
studentinfo(stno=2,sname='kumar',sectino='b',adders='knl')


# In[79]:


#gl
a=10
b=20
def add():
    c=a+b
    print(c)
def sub():
    c=b-a
    print(c)
def mul():
    c=a*b
    print(c)
def div():
    a=240
    c=a/b
    print(c)
    print(a)

add()
print("------------------")
sub()
print("**************")
mul()
print("===========")
div()


# In[87]:


a=10
b=20
def add():
    c=a+b
    print(c)
def add1():
    global a
    a=a+20
    c=a+b
    print(c)
    print(a)
        
add()
add1()


# In[33]:


#gloab variable
a=10
def add():
    b=int(input("enter a number:"))
    c=a+b
    print(c)
def sub():
    b=int(input("enter a number:"))
    c=b-a
    print(c)
def mul():
    b=int(input("enter a number:"))
    c=a*b
    print(c)
add()
sub()
mul()


# In[51]:





# In[91]:


a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
print("select your operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice=int(input("enter your choice:"))
if(choice==1):
    d=add(a,b)
    print("sum of ({}+{}={})".format(a,b,d))
elif(choice==2):
    d=sub(a,b)
    print("sub of ({}-{}={})".format(a,b,d))
elif(choice==3):
    d=mul(a,b)
    print("multiplication of ({}*{}={})".format(a,b,d))
elif(choice==4):
    d=div(a,b)
    print("Division of ({}/{}={})".format(a,b,d))
else:
    print("you entered invalid number try again")


# In[ ]:





# In[ ]:




