#!/usr/bin/env python
# coding: utf-8

# In[1]:


#set datatype
#The purpose of set datatype is that "To store multipe values  "
#empy set
a=set()
print(a)


# In[ ]:


#pre define function in set data type
"""
1.add()
2.clear()
3.copy()
4.discard()
5.remove()
6.pop()
7.is disjoint()
8.is subset()
9.is superset()
10.union()
11.intersection()
12.difference()
13.symmetric-difference()
14.update()  """


# In[4]:


#add function
#This element is used for adding element into set object
#syntax=setobj.add()
a={10,20,30,33.5,True,10}
print(a)
a.add(80)
print(a)
a.add(55)
print(a)


# In[7]:


#clear function
#This function is used for removing all the elements of set object
#syntax=setobj.clear()
a={10,20,30,40,50,55.6,22.3}
print(a)
a.clear()
print(a)
len(a)


# In[8]:


#copy function
#This function is used for copying the content of one setobject to another set objecj
#Syntax= setobj2=setobj1.copy()
a={10,20,30,40,50,60,10,20}
print(a)
b=a.copy()
print(b)


# In[11]:


#discard function
#Syntax=setobj.discard(element)
#This function is used for removing the specified element.
a={10,20,'vinod',True,55.63}
print(a)
a.discard(55.63)
print(a)


# In[16]:


#remove function
#Syntax=setobj.remove(element)
#This function is used for removing the specified element.
#If the element does not exists remove() gives KeyError
a={10,20,30,40,80,40}
print(a)
a.remove(40)
print(a)
a.remove(20)
print(a)
a.remove(66)         #KeyError: 66
print(a)


# In[27]:


#pop function
#This function is used for removing an arbitrary element from setobject
#Syntax=setobj.pop()
a={10,20,40,60,80}
print(a)
a.pop()
print(a)
a.pop()
a.pop()
a.pop()
a.pop()
print(a)
len(a)
a.pop()    #KeyError: 'pop from an empty set'


# In[28]:


#is disjoint function
#This function return True provided set objects are disjoint(no common elements) otherwise it returns False
s1={10,20,30,40}
s2={40,15,25,35}
s3={8,16,24,5}
s1.isdisjoint(s2)


# In[30]:


s1.isdisjoint(s3)


# In[32]:


#issubset function
#Syntax=   setobj1.issubset(setobj2)
#This function returns True provided all the elements of setobj1 present in setobj2. othetwise it returns False
s1={10,20,30,40}
s2={10,20,25,35}
s3={10,20}
s2.issubset(s1)


# In[34]:


s3.issubset(s1)


# In[38]:


#issuperset function
#Syntax=setobj1.issuperset(setobj2)
#This function returns True provided all the elements of setobj2 present in setobj1. othetwise it returns False
s1={10,20,30,40}
s2={10,20,25,35}
s3={10,20}
s1.issuperset(s2)


# In[39]:


s1.issuperset(s3)


# In[40]:


#union()
#Syntax=setobj3=setob1.union(setobj2)
#This functions obtains all the elements of setobj1 and setobj2 uniquely and place the result elements in setobj3
s1={10,20,30,40}
s2={40,50,60,70,30}
s1.union(s2)


# In[41]:


#Special Case
s1|s2    #is called Bitwise OR 


# In[42]:


#intersection()
#syntax=setobj3=setob1.intersection(setobj2)
#This functions obtains all the common elements from setobj1 and setobj2  and place the result elements in setobj3
s1={10,20,30,40}
s2={40,50,60,70,30}
s1.intersection(s2)


# In[45]:


#Special Case
s1&s2    #'&' is called bitwise AND


# In[46]:


#difference()
#syntax=setobj3=setob1.difference(setobj2)
#This function removes common elements from both setobj1 and setobj2 and takes remaining elements from setobj1 and place them in setobj3.
s1={10,20,30,40}
s2={40,50,60,70,30}
s1.difference(s2)


# In[47]:


s2.difference(s1)


# In[49]:


#special case
s1-s2
s2-s1      


# In[51]:


#Symmetric_difference()
#syntax=setobj3=setob1.Symmetric_difference(setobj2)
#This Function removes common elements from both setobj1 and setob2 and collect remaining elements from setobj1 and setobj2 and place them setobj3.
s1={10,20,30,40}
s2={40,50,60,70,30}
s1.symmetric_difference(s2)


# In[54]:


#special case
s2^s1    # here  ^ is called  Bitwise  XOR


# In[59]:


#update()
#syntax=setobj1.update(setobj2)
#This function adds all the valeus setobj2 to setobj1. 
s1={10,20,30,40}
s2={40,50,60,70}
s1.update(s2)
print(s1)
s2.update(s1)
print(s2)


# In[ ]:




