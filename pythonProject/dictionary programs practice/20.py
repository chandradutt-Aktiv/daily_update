"""
Write a Python program to print all unique values in a dictionary.
Go to the editor Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
 {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
"""

list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

d = set()

for i in (list1):
    print(i)
    for i,j in i.items():
        d.add(j)

print(d)
