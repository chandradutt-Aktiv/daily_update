# dictionary operations

dict1 = {1: 'abc', 2: 'xyz', 3: 'hello', 4: 'world'}
print(dict1.get(3))
print(dict1.items())
x = dict1.items()
dict1[4] = 'chandradutt'
print(x)
print(dict1.keys())
print(dict1)
print(dict1.pop(3))
print(dict1)

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
dict2 = {k: v for k, v in zip(keys, values)}
print(dict2)
print(dict(zip(keys, values)))

dict3 = {i: i ** 2 for i in values}
print(dict3)

sdi = {i.upper(): i * 3 for i in 'chandradutt'}
print(sdi)

newdict = {i: i ** 2 for i in range(10) if i ** 3 % 4 == 0}
print(newdict)

# import datetime

''' String Operations '''

str = 'HellO WorlD'
a = str[3 + 7]
b = 'L' + str[4:]
print(b)
print(a)
print(str[-6:-3])

# DateTime operations

# from datetime import date
from datetime import datetime, timedelta

current = datetime.today()
t = datetime.time(current)
print(t)
# print(date.now())
print(current.strftime("%d %B, %Y"))
print('minute:- ', current.minute, 'hour:- ', current.hour, 'second:- ', current.second, 'microsecond:- ',
      current.microsecond)
print(current.strftime("%H/%M/%S"))

n = datetime.now()
tdf = datetime.now() + timedelta(days=-10)
print(tdf)

print('maxtime', timedelta.max)
print('mintime', timedelta.min)

print('resolution', timedelta.resolution)
print(timedelta(days=365 * 2).total_seconds())

# Time after one second
time_after_one_minute = datetime.now() + timedelta(seconds=10) * 6
print(time_after_one_minute)

# absolute value timedelta
print('timedelta absolute value', abs(timedelta(days=+20)))

print('string representation of timedelta', str(timedelta(days=5, seconds=40, minutes=6, hours=20, microseconds=355)))

# Time delta usage

from datetime import datetime, timedelta
from pytz import timezone
import pytz

timezone = timezone('Asia/Calcutta')
normal = datetime(2021, 3, 16)
ambiguous = datetime(2021, 4, 16, 23, 30)

print('operations on normal datetime')
print(timezone.utcoffset(normal, is_dst=True))
print(timezone.tzname(normal, is_dst=True))

print('is_dst is false')
print(timezone.utcoffset(normal, is_dst=False))
print(timezone.tzname(normal, is_dst=False))

print('ambiguous datetime')
print(timezone.utcoffset(ambiguous, is_dst=True))
print(timezone.tzname(ambiguous, is_dst=True))

# ambiguous False
print('is_dst is false')
print(timezone.utcoffset(ambiguous, is_dst=False))
print(timezone.tzname(ambiguous, is_dst=False))

# datetime.timezone()

from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc
print(utc.zone)

India = timezone('Asia/Calcutta')
print(India.zone)

eastern = timezone('US/Eastern')
print(eastern.zone)

time_format = "%Y-%m-%d %h:%m:%s %Z%z"
