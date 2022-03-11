#!/usr/bin/env python
# coding: utf-8

# In[3]:


#print student marks repotr
while(True):
    stno=(int(input("Enter a number (1-----100):")))
    if(stno>0) and (stno<100):
        break
sname=input("Enter a student name ")
while(True):
    cm=int(input("Enter marks in c:"))
    if(cm>0) and (cm<100):
        break
while(True):
    cppm=int(input("Enter marks in cpp:"))
    if(cppm>0) and (cppm<100):
        break
while(True):
    pytm=int(input("Enter marks in pyt:"))
    if(pytm>0) and (pytm<100):
        break
totalmarks=cm+cppm+pytm
percentage=(totalmarks/300)*100
if((cm<40) or (cppm<40) or (pytm<40)):
    grade="fail"
else:
    if(totalmarks>=250) and (totalmarks<=300):
        grade="PASSED in DISTINCTION"
    elif(totalmarks>=200) and (totalmarks<=249):
        grade="PASSED  in FIRST"
    elif(totalmarks>=150) and (totalmarks<=199):
        grade="PASSED in SECOND"
    else:
        
        if(totalmarks>=120) and (totalmarks<=149):
            grade="Third class "
            
print("\t Student Marks Report:")
print("\t student Number:{}".format(stno))
print("\t student Name:{}".format(sname))
print("\t student marks in c:{}".format(cm))
print("\t student marks in cpp:{}".format(cppm))
print("\t student marks in pyhton:{}".format(pytm))
print("\t student Total marks :{}".format(totalmarks))
print("\t student percentage:{}".format(percentage))
print("\t student Greade:{}".format(grade))


# In[13]:


#given number is prime or not prime
n=int(input("enter a number"))
if(n<=1):
    print("{} is invalid input:".format(n))
else:
    result=True
    for i in range(2,n):
        if(n%i==0):
            result=False
            break
    if(result):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))

            
            


# In[14]:


n=int(input("enter a number "))
if(n<=0):
    print("you entered invalid number try again")
else:
    for n in range(2,n+1):
        for i in range(1,11):
            print("{} x {} ={}".format(n,i,n*i))
        


# In[ ]:




