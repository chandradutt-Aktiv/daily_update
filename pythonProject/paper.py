"""
write a function to extract words from the sentence that are repeated multiple times.
the function must return values display those words with "#" seperator
(use .join function) for example WORD1#WORD2#WORD3
"""
"""
def f1():
    str = 'hello world good world best world hello good world'
    l2=[]
    l1 = str.split()
    l2=[i for i in l1 if(l1.count(i)>1 and i not in l2)]
    for i in l1:
        if(l1.count(i)>1 and i not in l2):
            l2.append(i)
    print("#".join(l2))
f1()"""


"""
write a program to extract string elements from a list based on below conditions.
use in-built functions.
    a.First character must capitalize and consonant.
    b.string must not contain any number.
"""
"""
str = 'The Fox Is In The Jungle'
str = str.split()
l=['A','E','I','O','U']
def fun(st):
    out=[]
    for i in str:

        if (i.istitle()):
            if(i.isalpha() and i[0] not in l):
                out.append(i)
    return out

print(fun(str))
"""

"""
l1 = [5600,12,5432,764,9876,1234,342]
for i in range(len(l1)):
    if(len(str(i))==4):
        first = i/1000
        last = i%10
        if(first%2 != 0 and last%2 == 0):
            if(i%3==0 or i%7==0):
                print(l1)
"""


# Q-4
employees = {
    'PM':{
        'Robert_Downey':{
            'TL':
                {'Mark':{'exp':8},'Samual':{'exp':8},'Paul':{'exp':8},'Tom':{'exp':8}}
        },

        'Anney_Hathaway':{
            'TL':
                {'Chris':{'exp':5},'Pratt':{'exp':5},'Emma':{'exp':5},'Will':{'exp':5},'Smith':{'exp':5}
            }
        }
    },
    'Manager':{
        'Chris':
            {'S_dev':{'Jennifer':{'exp':3.8},'Scott':{'exp':3.8},'Sophie':{'exp':3.8}},
        },
        'Will':
            {
                'S_dev':{'Edge':{'exp':3},'Ryan':{'exp':3.5}}
        }
    },
    'Mentor':{
        'Paul':{
            'S_dev':{'Fergal':{'exp':4.5}}
        },

        'Tom':{
            'J_dev':{'Jerry':{'exp':1.5}, 'James':{1.6}}
        },
        'Mark':{
            'J_dev':{'Leonardo':{'exp':1}, 'Alexandra':{'exp':1}}
        }
    },
    'Reporting_manager':{
        'Smith':{
            'S_dev':{'Walker':{'exp':2.7}, 'Diana':{'exp':2.7}}
        }
    }
}

# a.
def a():
    """
    employees1 = employees['PM']['Anney_Hathaway']['TL']
    print(employees1)
    """
    for i in employees:
        print(i)
        for j in employees['PM']:
            for k in employees['PM']['Robert_Downey']:
                for l in employees['PM']['Robert_Downey']['TL']:
                    print(list(l))
a()
# b.
