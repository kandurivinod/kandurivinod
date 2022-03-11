#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
school={'School_name': 'hps',
        'website': 'http://hps.com',
        'Email':'hps123@gmail.com',
        'location': 'https://www.ushodayhighschool.com',
       'phone_number': 8143635849,
        'principle': 'vinod',
        'School_Address': {'city': 'kurnool',
                           'village': 'yerraguntla',
                           'pincode':518573},
        'sttaf': [ 
            {
            'name': 'kumar',
            'phone_number': 1234567890,
            'subject':['maths','englis'],
            'role': 'Teacher'
            },
            {
                'name': 'balaji',
                'phone_number': 4561237890,
                'subject':['Telugu','social'],
                'role': 'Teacher'
            },
        {
            'name': 'sivakrishnays',
            'phone_number': 7894561230,
            'subject':['Hindi','science'],
            'role':'Teacher'
        },
        {
            'name': 'madhu',
            'phone_number': 9874561230,
            'subjects':['Telugu','Hindi'],
            'role':'Teacher'
        },
            
        {
            'name': 'madhuri',
            'phone_number': 8794562102,
            'subjects':['maths','social'],
            'role':'Teacher'
        },
        {
            'name': 'Gangadhar',
            'phone_number': 7984562013,
            'subjects':['Science','English'],
           'role':'Teacher'
            },
        ],
        'Non_techingstaff': [
        {
        'name': 'Asmitha',
            'phone_number': 9578445647,
            'role': 'Attender'},
        {
        'name':'umar',
        'phone_number': 8547961423,
        'role': 'PETmaster'},
        ],
        'Fee':{
                '1stclass': 10000,
                '2ndclass': 15000,
                '3rdclass': 20000,
                '4thclass': 25000,
                '5thclass': 30000,
                '6thclass': 35000,
                '7thclass': 40000,
                '8thclass': 45000,
                '9thclass': 50000,
                '10thclass': 55000
            },
        
        'Students':[
            {
            'Roll_Number':1,
            'Student_Name':'vinod',
            'Phone_number':9638527410,
            'Marks':{
            'Telugu':60,
            'Hindi':40,
            'English':78,
            'MATHS':96,
            'science':63,
            'social':63,
            'Percentage':None
            }
            },
        {
            'Roll_Number':2,
            'Student_Name':'kumar',
            'Phone_number':9638527410,
            'Marks':{
            'Telugu':60,
            'Hindi':40,
            'English':78,
            'MATHS':96,
            'science':63,
            'social':63,
            'Percentage':None
            }
        },
        {
            'Roll_Number':3,
            'Student_Name':'Priya',
            'Phone_number':8549761235,
            'Marks':{
            'Telugu':78,
            'Hindi':47,
            'English':79,
            'MATHS':69,
            'science':36,
            'social':43,
            'Percentage':None
            }
        },
        {
            'Roll_Number':4,
            'Student_Name':'kumar',
            'Phone_number':7345891627,
            'Marks':{
            'Telugu':55,
            'Hindi':45,
            'English':73,
            'MATHS':81,
            'science':46,
            'social':54,
            'Percentage':None}},
        {
            'Roll_Number':5,
            'Student_Name':'kumar',
            'Phone_number':9647581223,
            'Marks':{
            'Telugu':68,
            'Hindi':54,
            'English':45,
            'MATHS':63,
            'science':78,
            'social':45,
            'Percentage':None}},
        {
            'Roll_Number':6,
            'Student_Name':'Teja',
            'Phone_number':7143568970,
            'Marks':{
            'Telugu':37,
            'Hindi':85,
            'English':87,
            'MATHS':63,
            'science':77,
            'social':63,
            'Percentage':None
            }
        },
        {
            'Roll_Number':7,
            'Student_Name':'Asmitha',
            'Phone_number':9564123789,
            'Marks':{
            'Telugu':65,
            'Hindi':45,
            'English':92,
            'MATHS':64,
            'science':62,
            'social':85,
            'Percentage':None}
        },
        {
            'Roll_Number':8,
            'Student_Name':'Madhu',
            'Phone_number':8546321789,
            'Marks':{
            'Telugu':66,
            'Hindi':43,
            'English':58,
            'MATHS':62,
            'science':58,
            'social':45,
            'Percentage':None
            }},
        {
            'Roll_Number':9,
            'Student_Name':'Manoj',
            'Phone_number':7056412398,
            'Marks':{
            'Telugu':60,
            'Hindi':43,
            'English':48,
            'MATHS':66,
            'science':75,
            'social':83,
            'Percentage':None
            }
        },
        {
            'Roll_Number':10,
            'Student_Name':'sai prasad',
            'Phone_number':9704651247,
            'Marks':{
            'Telugu':69,
            'Hindi':41,
            'English':38,
            'MATHS':86,
            'science':66,
            'social':53,
            'Percentage':None
            }
        },
        {
            'Roll_Number':11,
            'Student_Name':'Vara lakshmi',
            'Phone_number':853143970,
            'Marks':{
            'Telugu':60,
            'Hindi':40,
            'English':72,
            'MATHS':95,
            'science':45,
            'social':74,
            'Percentage':None
            }
        },
        ]
        
         
       }
f = json.dumps(school) 
print(f)


# In[ ]:




