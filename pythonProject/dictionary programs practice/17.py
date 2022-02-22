"""Write a Python program to remove duplicates from Dictionary."""
"""r={}
d={4:5,8:6,1:1,2:4,5:3,3:9,1:5}
for key,value in d.items():
    if(value not in r.values()):
        r[key]=value
print(r)
"""
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for i in student_data.items():
    for j in student_data.values():
        for k in student_data.values():
            if(k.values()=='Sara'):
                print(k)


for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
