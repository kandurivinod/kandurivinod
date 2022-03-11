#!/usr/bin/env python
# coding: utf-8

# In[4]:


# using if statement findig bigest element
a=int(input("enta a first number"))
b=int(input("enter a secon number"))
c=int(input("enter a third number"))
if(a>b) and (a>c):
    print("bigest element is{}".format(a))
if(b>a) and (a>c):
    print("bigest element is {}".format(b))
if(c>a) and (c>b):
    print("bigest element is {}".format(c))
if(a==b==c):
    print("all numbers are equal")
"""
enta a first number10
enter a secon number20
enter a third number30
bigest element is 30 """


# In[6]:


# using if else statement finding biggest number (or) equal
a=int(input("enter a first number"))
b=int(input("enter a second number"))
if(a==b):
    print("Both are equal")
else:
    if(a>b):
        print("{} is graterthan of {} ".format(a,b))
    else:
        print("{} is grater than of {}".format(b,a))
"""
enter a first number10
enter a second number20
20 is grater than of 10 """


# In[8]:


#if  elif else statement 
n=int(input("enter a number "))
if(n==0):
    print("{} is zero".format(n))
elif(n==1):
    print("{} is One".formt(n))
elif(n==2):
    print("{} is Two".format(n))
elif(n==3):
    print("{} is Three".format(n))
elif(n==4):
    print("{} is Four ".format(n))
elif(n==5):
    print("{} is Five".format(n))
elif(n==6):
    print("{} is Six".format(n))
elif(n==7):
    print("{} is seven".format(n))
elif(n==8):
    print("{} is Eight ".format(n))
elif(n==9):
    print("{} is nine".format(n))
else:
    print("{} is Number".format(n))
print("program finshed ")
"""
enter a number 5
5 is Five
program finshed """


# In[ ]:




