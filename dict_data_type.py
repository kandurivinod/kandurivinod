#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dict data type
#"dict" is one of the pre-defined class and  treated as dict data type.
# The purpose of ditc data type is that "To store the data in the form (Key,Value)"
"""
a)clear()
b)pop()
c)popitem()
d)copy()
e)get()
f)values()
g)keys()
h)items()
i)update()    """


# In[2]:


#empty dict
a=dict()
print(a,type(a))    #{} <class 'dict'>

b={}
print(b,type(b))    #{} <class 'dict'>


# In[5]:


#clear()
#This function clears / removes all the elements of  dict object
#Syntax=dictobj.clear()
a={10:'vinod',20:'manoj',30:'apple',40:'sun'}
print(a,type(a))      #{10: 'vinod', 20: 'manoj', 30: 'apple', 40: 'sun'} <class 'dict'>
len(a)                #4
a.clear()
print(a)               #{}


# In[15]:


#pop()
#This is used for removing (key,value) from dict object bassed on key, which we passing.
#If the key does exists in dict object then we get KeyError.
#syntax=dictobj.pop(key)
a={10:'balu',20:'siva',30:'madhu',40:'murali'}
a.pop(20)
print(a)
a.pop(100)             KeyError: 100    


# In[16]:


#popitem()
#This function removes last (key,value) of dict object when it is non-empty
#othertwise we get  KeyError: 'popitem(): dictionary is empty'
#Syntax=dictopbj.popitem()
a={10:'mounika',20:'krishna',30:'teja',40:'balu'}
print(a)
a.popitem()     #(40, 'balu')
a.popitem()     #(30, 'teja')
a.popitem()    #(20, 'krishna')
a.popitem()    #(10, 'mounika')
a.popitem()    #KeyError: 'popitem(): dictionary is empty'


# In[21]:


#copy()
#This function copy the content of one dict object into another dict object.
#Syntax=dictobj2=dictobj1.copy()
d1={10: 'Guava', 20: 'Mango', 30: 'Kiwi', 40: 'sberry'}
print(d1)
d2=d1.copy()
print(d2)


# In[28]:


#get()
#This function is used for obtaining value of Value by Passing Value of Key.
#If the Value of Key does not exist then Value of Value is "None"
#syntax=Value=dictobj.get(key)
d={10:'vinod',20:'sravani',30:'kiwi',40:'siva'}
print(d)
d.get(10)       #'vinod'
d.get(20)       #'sravani'
d.get(30)       #'kiwi'
d.get(60)


# In[32]:


#values()
#This obtains all the values of dict object
#syntax=values=dictobj.values()
d={10: 'Guava', 20: 'Mango', 30: 'Kiwi', 40: 'sberry',50:'vinod'}
print(d)
d.values()    #dict_values(['Guava', 'Mango', 'Kiwi', 'sberry', 'vinod'])
a=d.values()
print(a)      #dict_values(['Guava', 'Mango', 'Kiwi', 'sberry', 'vinod'])
for b in a:
    print(b)         #Guava
                     #Mango
                     #Kiwi
                     #sberry
                     #vinod


# In[36]:


#keys()
#This obtains all the keys  of dict object.
#syntx=keys=dictobj.keys()
d={10:'vinod',20:'kumar',30:'suman',40:'mounika',50:'teja'}
print(d)
d.keys()    #dict_keys([10, 20, 30, 40, 50])
a=d.keys()
print(a)     #dict_keys([10, 20, 30, 40, 50])
for b in a:
    print(b)
                  #10
                  #20
                  #30
                  #40
                  #50


# In[41]:


#items()
#This obtains obtains all (key,value) from dict object.
#syntax= keysvalues=dictobj.items()
d={10:'vinod',20:'kumar',30:'suman',40:'mounika',50:'teja'}
print(d)
d.items()      #dict_items([(10, 'vinod'), (20, 'kumar'), (30, 'suman'), (40, 'mounika'), (50, 'teja')])
a=d.items()
for b,c in a:
    print(b,"---->",c)     
                             #10 ----> vinod
                             #20 ----> kumar
                             #30 ----> suman
                             #40 ----> mounika
                             #50 ----> teja
                 


# In[46]:


#update()
#This function update the (key,value) of dictobj1 with (key,value) of dictobj2.
#syntax=dictobj1.update(dictobj2)
d1={10:1.2,20:2.3}
d2={30:4.5,40:5.6}
d1.update(d2)       #{10: 1.2, 20: 2.3, 30: 4.5, 40: 5.6}
print(d1)
print(d2)
d2.update(d1)
print(d2)            #{30: 4.5, 40: 5.6, 10: 1.2, 20: 2.3}


# In[ ]:




