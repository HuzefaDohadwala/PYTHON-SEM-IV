'''Given a tuple of elements, write a python program to create 
a dictionary with tuple elements as a key and its count in 
tuple as value e.g t = (4,5,6,2,3,4,5,1,2,6,4) then output 
should be d = {4:3,5:2,2:2,3:1,1:1}
'''

t = (4,5,6,2,3,4,5,1,2,6,4)
keys = []
values = []
d1 = {}
for i in t:
    if i not in keys:
        keys.append(i)
        
for j in keys:
    n = t.count(j)
    values.append(n)

for i in range(len(keys)):
    d1[keys[i]] = values[i]
print(d1)

''' output 
{4: 3, 5: 2, 6: 2, 2: 2, 3: 1, 1: 1}
'''

'''Write a python program to print tuple of website suffixes 
from given dictionary 
{ 1:"www.yahoo.com",
  2:"www.tsec.edu",    
  3:"www.asp.net",
  4:"www.abcd.in"}
'''

d2 = {
  1:"www.yahoo.com",
  2:"www.tsec.edu",    
  3:"www.asp.net",
  4:"www.abcd.in"}

suffixes = []

for url in d2.values():
    suffix = url.split(".")[-1]
    suffixes.append(suffix)
print(tuple(suffixes))

''' output 
('com', 'edu', 'net', 'in')
'''