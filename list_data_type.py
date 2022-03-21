#!/usr/bin/env python
# coding: utf-8

# In[6]:


s='vinod'
s[0]
s[1]
s[2]
s[3]
s[4]
s[5]


# In[10]:


s[0:6:2]


# In[14]:


w=input("enter wors")
i=0
for i in w:
    print(i)
    


# In[15]:


b=input("Enter one sentences")
for i in b[::]:
    print(i,end=(' '))


# In[18]:


a=input("Enter one sentences:")
for j in a[::-1]:
    print(j,end=(''))


# In[19]:


#replace function
s="python is so diffuclate"
s1=s.replace("diffuclate","easy")
print(s1)


# In[20]:



#replacev="balaji is a bad boy."
e=v.replace("bad","good")
print(e)


# In[26]:


#split function
l="balaji is a good boy."
m=l.split()
for i in m:
    print(i)


# In[28]:


#split function
v="my name is vinod kumar and i complated post gradutation."
l=v.split()
for i in l:
    print(i)


# In[35]:


#split function
d='21-3-2022'
o=d.split('-')
for i in o:
    print(i)


# In[37]:


#join string
l=('vinod','kumar','kanduri')
t='-'.join(l)
print(t)


# In[42]:


#changing case of string
l='my name is vinod kumar'
print(l.lower())
print(l.upper())
print(l.title())
print(l.swapcase())
print(l.capitalize())


# In[45]:


word=input("Enter a word")
d=[]
for i in word:
    if i not in d:
        d.append(i)
        s=''.join(d)
print(s)


# In[47]:


n=input("Enter a string:")
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)


# In[48]:


n=int(input("Enter a number:"))
k=[]
for i in range(n):
    if i%2==0:
        k.append(i)
print(k)        


# In[50]:


n=int(input("Enter a number"))
g=[]
for i in range(n):
    if i%2 !=0:
        g.append(i)
print(g)


# In[61]:


"""Q. Write a program to accept student name and marks from the keyboard 
and creates a dictionary. Also display student marks by taking student name 
as input? """
n=int(input("Enter number of students"))
d={}
for i in range(n):
    name=input("Enter student name")
    marks=int(input("enter student marks"))
    d[name]=marks
print(d)


# In[62]:


name=input("enter name:")
d[name]


# In[57]:


n=input("enter sentances:")
vowels={'a','e','i','o','u'}
d={}
d1=[]
for i in n:
    if i in vowels:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    else:
        d1.append(i)
print(d)
print(d1)


# In[ ]:




