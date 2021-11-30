# https://docs.pyhton.org/3.10/library/datatime.html

from datetime import datetime, timedelta

data = datetime(2019, 4, 20, 10, 23, 20)

print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

print('*' * 100)

data1 = datetime.strptime('20/04/2021', '%d/%m/%Y')
print(data1)
print(data1.timestamp())

print('#' * 100)

data2 = datetime.fromtimestamp(1618887600.0)
print(data2)

'''

'''




