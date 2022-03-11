#!/usr/bin/env python
# coding: utf-8

# In[1]:


# using while loop print math table
n=int(input("enter a number"))
if(n<=0):
    print("you entered invalid number try again")
else:
    i=1  # initlizatioon part
    while(i<=10): #condition part
        print("{}*{}={}".format(n,i,i*n))
        i=i+1 # incrementtatioon part
        


# In[2]:


#find the even numbers using while loop
n=int(input("enter a number "))
if(n<=0):
    print("you entered invalid number tyr again")
else:
    print("Even numbers within {}".format(n))
    i=2  #initlizatioon part
    while(i<=n): #condition part
        print("even number is {}".format(i))
        i=i+2 #increment
    else:
        print("This is else part")


# In[3]:


#find factorial of a given number 
num=int(input("enter a number"))
if(num<=0):
    print("you entered invaild number  try again")
else:
    i=1
    r=1
    while(i<=num):
        r=r*i
        i=i+1
    else:
        print(" Factorial of  {} is {}".format(num,r))


# In[4]:


#The given number to print reverse number using while loop
n=int(input("enter a number "))
if(n<=0):
    print("you enter invalid number try again")
else:
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    else:
        print("Reverse order is {}".format(r))
    
    


# In[5]:


#check given number is palindrome or not palindrome
n=int(input("enter a number "))
if(n<=0):
    print("you entered invalid number try again " )
else:
    tn=n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    else:
        if(tn==r):
            print("given number is palindrome {}".format(r))
        else:
            print("given number is not palindrome {}".format(r))
        


# In[ ]:




