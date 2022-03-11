#!/usr/bin/env python
# coding: utf-8

# In[3]:


# byte is one of the predefine class and terated as sequence data type and   range (0 to 255)
a=[1,10,20,30,256]
print(a,type(a))
b=bytes(a)


# In[9]:


a=[10,20,30,40,255]
print(a,type(a))
b=bytes(a)
print(b)
for c in b:
    print(c)


# In[7]:


a=[10,20,-20,-30]
b=bytes(a)


# In[10]:


a=[10.0,20.0,30,40,50,60]
b=bytes(a)


# In[12]:


a=[10,20,0,40,255,234]
b=bytes(a)
print(b)
for c in b:
    print(c)


# In[15]:


# Range data type the purpose of range data type is to store the sequential values with equal interval

# syntax1=range(begin)

a=range(10)
print(a)
for b in a:
    print(b)
    


# In[18]:


# syntax2=range(begin,end) 
a=range(10,21)
print(a)
for b in a:
    print(b)


# In[21]:


# syntax3=range(begin,end,step)
a=range(20,31,2)
print(a)
for b in a:
    print(b)


# In[26]:


for a in range(10,0,-1):
    print(a)


# In[29]:


for a in range(100,201,20):
    print(a)


# In[ ]:


"""pre-define functions in list
1.append()
2.insert()
3.copy()
4.remove()
5.pop(index)
6.pop()
7.clear()
8.index()
9.reverse()
10.sort() """


# In[49]:


#list datatype
# list is one of the pre-define class and treated list datatype
# The purpose of list data type is that "To store multiple values either of same datatype and different datatype or both the types with Unique and Duplicate Values". "




m=list()         #empty list
print(m,type(m))
n=[]              #empty list
print(n,type(n))


# In[ ]:


#append function

# syntax=listobj.append(element)

l=[10,20,-30,'vinod',2+3j,True]
print(l)
l.append('kumar')
print(l)
l.append('mounika')
print(l)
l.append(55)
print(l)


# In[43]:


# To add the variable into a list 

#insert function

# syntax=listobj.insert(index,element)

a=[10,30,20,0,55,-30,'vinod',True]
print(a)
a.insert(0,'kumar')
print(a)
a.insert(-1,'mouni')
print(a)


# In[50]:


#copy function

#this function is used to copying the  content one list to anoter list

#syntax=listobj2=listobj1.copy()

a=[10,20,-30,5+2j,'vinod',True]
b=a.copy()
print(b)
print(a)


# In[53]:


#remove function

#This function is used for removing element in list

#syntax=listob.remove(element)

a=[10,20,30,50,10]
print(a)
a.remove(10)
print(a)
a.remove(55)  #list.remove(x): x not in list
print(a)


# In[58]:


# pop(index) function

#This function is used for removing element of list object

#syntax=listobj.pop(index)
a=[10,20,30,'vinod',3+5j,True,55.63]
print(a)
a.pop(0)
print(a)
a.pop(3)
print(a)
a.pop(6)  #IndexError: pop index out of range
print(a)


# In[71]:


# pop function
# This function is used for removing last element of list object
#syntax=listobj.pop()
a=[10,5+3j,66.53,True]
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
a.pop()
print(a)
a.pop()   #IndexError: pop from empty list
print(a)


# In[73]:


#clear function 
#This function is used for removing/clearing all the elements of list object.
#syntax=listobj.clear()
a=[10,20,55.63,3+5j,'vinod',True]
print(a)
a.clear()
print(a)
len(a)


# In[78]:


#del function 
#del() is used for deleting the element based on Index , range of values and it can also delete object.
a=[10,20,30,'vinod',5+3j,True,55.63]
print(a)
del(a[1])
print(a)
del(a)
print(a)  # NameError: name 'a' is not defined


# In[82]:


#index function
#This function is used for finding index of first occurence of specified element.
#synta=listobj.index(element)
a=[10,20,30,55.63,'vinod',True,10,20,30]
print(a)
a.index(20)
a.index(300)     #ValueError: 300 is not in list


# In[83]:


#count function
#this function is used for finding number of occurences of specifed elements
#syntax=listobj.count(element)
a=[10,20,30,50,40,10,20,30,'vinod',True,55.6]
a.count(10)


# In[84]:


a.count(20)


# In[85]:


a.count('vinod')


# In[86]:


a.count(333)


# In[87]:


# reverse function
# This function is used for revers the element fornt to back
#syntax=listobj.reverse()
a=[10,20,30,40,50,80,'vinod',5+3j,55.6,True]
a.reverse()
print(a)


# In[89]:


#sort function
# This function is used for homogeneous elements of listobject
#syntax=listobj.sort()
a=[10,20,-3,-8,9,25.6,88,23,0]
a.sort()
print(a)


# In[90]:


a=[10,20,-8,-9,30,40,'vinod',True]
a.sort()
print(a)    #TypeError: '<' not supported between instances of 'str' and 'int'


# In[98]:


#Inner List (or) nested list
#The process of defining one or more number of lists in another list is known as Inner / Nested List.
#syntax=listobj=[val1,val2......[v1,v2...v-n],[x1,x2...xn], val-n  ]
lst=[10,"Abhi", [18,19,17] ,[50,80,70], "OUCET"]
print(lst)
print(lst[0])
print(lst[-1])
print(lst[-2])


# In[ ]:




