#!/usr/bin/env python
# coding: utf-8

# In[3]:


d={'name':'vinod',
       'age':23,
       'dob':11-6-1995}


# In[7]:


def main(personal_data):
    d=[]
    d.append(personal_data)
    return d
main(d) 


# In[6]:


d={10:'vinod'}
print(d)


# In[13]:


d={'name':'vinod',
  'dob':11-6-1997,
  'phone_number':9160635849,
  'add':'nandyal'}
print(d)


# In[15]:


n=[]
n.append(d)
print(n)


# In[43]:


print(a,type(a))


# In[44]:


print(id(a),a=)


# In[45]:


a1='vinod kumar'


# In[46]:


c=a1[1:5:2]


# In[47]:


c


# In[48]:


a[3]


# In[49]:


s="Learning Python is very very easy!!!"


# In[50]:


s[1:7:1] 


# In[51]:


n=10
d=[]
for i in range(n):
    if i%2==0:
        print(i)
        d.append(i)
    else:
        pass
d   


# In[52]:


n=10
for i in range(n):
    if (i%2!=0):
        print(i)
        


# In[53]:


a=10
b=10
print(id(a))
print(id(b))


# In[54]:


a=10+5j
b=10+5j
print(id(a))
print(id(b))
a is b
a is not b


# In[55]:


a='vinod'
b='vinod'
print(id(a))
print(id(a))
a is b
a is not b
a in b
a not in b


# In[56]:


dict=['INDTGHYD','INDTGWNL','INDAPGN', 'INDAPONL']
for i in dict:
    print(i)
    c=i[3:5]
    print(c)


# In[57]:


dict=['INDTGHYD','INDTGWNL','INDAPGN', 'INDAPONL']
d={}
for i in dict:
    if i[3:5] not in d:
        d[i[3:5]]=[i[5:8]]
    else:
        d[i[3:5]].append(i[5:8])
        
d


# In[58]:


l=[10,20,30]
l[0]=100
print(l)
for i in l:
    print(i)


# In[59]:


d={'vinod':10,'kumar':20}
print(d)
d['vinod']=60
print(d)
d['balu']=60
print(d)


# In[60]:


a=10
b=2
print(a+b)


# In[61]:


n=-2
if(n<=0):
    print(n)
else:
    print(n)


# In[62]:


a=20
b=10
a>b


# In[63]:


a=10
b=11
if(a!=b):
    print('not equal')
else:
    print("equal")


# In[64]:


a=10
a+=1
print(a)


# In[65]:


a=20
a&=2
print(a)


# In[66]:


a,b=[int(x) for x in input("enter 2 numbers:").split()]
print(a*b)


# In[67]:


a,b=[int(x) for x in input().split()]


# In[68]:


eno=int(input("enter employee number:"))
ename=input("enter employee name:")
esal=float(input("enter employee salary:"))
edd=input("enter employee address:")
married=bool(input("Employee Married [True|False]:"))
print("please information:")
print("Enter Employee Number:{}".format(eno))
print("Enter Employee Name:{}".format(ename))
print("Enter Employee salary:{}".format(esal))
print("Enter Employee Address:{}".format(edd))
print("Employee Married :{}".format(married))


# In[70]:


a,b=[int(x) for x in input("enter two number").split(',')]
print("{}*{}={}".format(a,b,a*b))


# In[71]:


x=eval("10+20+30")
print(x)


# In[72]:


x=eval("(10*20+30)**50")
print(x)


# In[73]:


a,b,c=10,20,30
print(a,b,c,sep=':')


# In[74]:


print("vinod")
print("kumar")
print("kvk")


# In[75]:


print("vinod",end='')
print("kumar",end='')
print("kvk")


# In[76]:


l=[10,20,30,40]
t=(10,20,30,40)
print(l)
print(t)


# In[77]:


s="vinod"
d=25
s1="java"
s2="python"
print("hello",s,"your age is",d, )
print("your teaching ",s1,"and",s2,)


# In[78]:


name=input("enter name:")
if(name=='vinod'):
    print("{} good afternoon ".format(name))
print("How are you {}".format(name))




# In[79]:


name=input("enter your name:")
if(name=='vinod'):
    print("Hello good moring {}".format(name))
else:
    print("Hello gest good moring ")
print("How are you!!!")


# In[80]:


n=int(input("enter a number"))
if n%2==0:
    print("given number is even")
else:
    print("given number is odd")


# In[83]:


n=int(input("enter number:"))
if (n>=1) and (n<=100):
    print("given number is correct")
else:
    print("given number is wrong")


# In[84]:


#Write a program to find smallest of given 2 numbers?
a=int(input("enter a first number "))
b=int(input("enter a first number"))
if(a<b):
    print("{} is samllest number".format(a,b))
else:
    print("{}  is smallest number".format(b,a))


# In[86]:


#Write a program to find smallest of given 3 numbers?
a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
c=int(input("enter a third number"))
if (a<b) and (a<c):
    print("smallest number is {}".format(a))
elif (b<c) and (b<a):
    print("smallest number is {}".format(b))
else:
    print("smallest number is {}".format(c))


# In[87]:


n=int(input("Enter a number:"))
if(n==0):
    print("{} is zero".format(n))
elif(n==1):
    print("{} is one".format(n))
elif(n==2):
    print("{} is Two".format(n))
elif(n==3):
    print("{} is Three".format(n))
elif(n==4):
    print("{} is four".format(n))
elif(n==5):
    print("{} is five".format(n))
elif(n==6):
    print("{} is six".format(n))
elif(n==7):
    print("{} is sveven".format(n))
elif(n==8):
    print("{} is eight".format(n))
elif(n==9):
    print("{} is Nine".format(n))
else:
    print("you are given number:{}".format(n))


# In[89]:


s='vinod kumar'
for i in s:
    print(i)


# In[91]:


n=int(input("enter a number"))
for i in range(n):
    print(i)


# In[92]:


list=eval(input("Enter list:"))
sum=0
for x in list:
    sum+=x
    print(sum)


# In[93]:


n=int(input("enter a number:"))
sum=0
i=0
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)


# In[49]:


for x in range(11):
    print("hello")


# In[53]:


name=""
while name!="vinod":
    name=input("enter name:")
print("thanks for information")
    


# In[56]:


d={'name':'vinod',
  'dob':11-6-1997,
  'age':25}
print(d)


# In[61]:


def main(persional_data):
    d=[]
    d.append(persional_data)
print(d)
main(d)


# In[63]:


s1=input("Enter a first string:")
s2=input("Enter a second string:")
if (s1<s2):
    print("biggest string is {}".format(s1))
elif (s1>s2):
    print("biggest string is {}".format(s2))
else:
    print("all strings are equal")
    


# In[77]:


s='   nandyal'
c=s.strip()
print(c)
s.count('a')


# In[80]:


l='my name is vinod kumar and i am comming from nandyal'
a=l.split()
for x in a:
    print(x)


# In[83]:


t=['vinod','kumar','kanduri']
s='-'.join(t)
print(s)


# In[1]:


list=[]
print(list)
print(type(list))


# In[94]:


list=eval(input("Enter list"))
print(list)
print(type(list))


# In[24]:


l=list(range(0,10,2))
print(l)
print(type(l))


# In[16]:


l="vinod"
k=list(l)
print(k)


# In[98]:


import re
l='vinod-kumar&kanduri'
k=l.split('-,&')
print(k)


# In[16]:


c=list(range(0,10,2)) 
print(c) 
print(type(c)) 


# In[17]:


n=[int(x) for x in input(" ").split(",")]


# In[18]:


n


# In[103]:


l=[10,20,30,[50,60,70]]
print(l)
l[3][2]


# In[107]:


n=[1,2,3,4,5,6,7,8,9]
t=n[4::2]
print(t)


# In[109]:


t=n[3:7]
print(t)


# In[112]:


t=n[8:2:-2]
print(t)


# In[113]:


t=n[4:100]
print(t)


# In[115]:


n=[10,20,30,40]
print(n)
n[1]=777
print(n)


# In[132]:


n=[1,2,3,4,5,6,7,8,9]
len(n)
i=0
while i<len(n):
    print(n[i])
    i+=1


# In[133]:


for n1 in n:
    print(n1)
    


# In[135]:


i=[1,2,3,4,5,6,7,8,9]
for n1 in n:
    if(n1%2==0):
        print(n1)


# In[137]:


l=[10,20,30,40]
t=len(l)
print(t)


# In[143]:


n=[1,2,2,3,3,1,6,7,8,6,7,8]
print(n)
print(n.count(1))
print(n.count(8))
n.count(2)


# In[149]:


n=[1,2,2,2,1,3,3,3,6,7,8,9,6,7,8,9]
print(n.index(1))
print(n.index(2))
print(n.index(6))
print(n.index(8))
print(4 in n)


# In[151]:


l=[]
l.append('a')
l.append('b')
l.append('c')
l.append('d')
print(l)


# In[156]:


l=[]
for i in range(101):
    if i%10==0:
        l.append(i)
        print(l)


# In[159]:


l=[]
for i in range(31):
    l.append(i)
print(l)


# In[164]:


l=[]
for i in range(20):
    if i%2==0:
        l.append(i)
print(l)


# In[169]:


l=[10,20,30,40,50,60]
print(l)
l.insert(10,500)
print(l)
l.insert(-10,600)
print(l)


# In[180]:


l=['vinod']
l1=['kumar']
l.extend(l1)
print(l)


# In[172]:


order1=["Chicken","Mutton","Fish"] 
order2=["RC","KF","FO"] 
order1.extend(order2) 
print(order1)


# In[179]:


l=['vinod','kumar']
l.extend('goodmoring')
print(l)


# In[184]:


l=[10,20,30,10,20,30,40,50,60,40,50,60]
l.remove(30)
l.remove(30)
print(l)


# In[191]:


l=[10,20,30,40,50]
print(l)
l.pop()
l.pop()
l.pop()
l.pop()
l.pop()
l.pop()


# In[193]:


n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("element row wise")
for r in n:
    print(r)
print("element by matrix style ")
for i in


# In[194]:


n=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(len(n)):
    print(i)


# In[219]:


n=[[10,20],[40,50,60],[70,80,90]]
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()


# In[215]:


n=[[10,20],[40,50],[70,80]]
len(n[i])


# In[227]:


n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("Element of row wise")
for r in n:
    print(r)
print("Element of matrix ")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()


# In[239]:


s=[x*x for x in range(1,5)]
print(s)


# In[234]:


range(5)


# In[238]:


range(5)


# In[ ]:




