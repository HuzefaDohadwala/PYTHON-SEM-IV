'''
Write a python program to create a list where the number of elements 
are taken from the user. Further add even numbers from list and odd 
numbers from list. These two numbers should be displayed as tuples.
'''
list1=[]
n=int(input("enter no of ele :"))
for i in range(0,n):
    q=int(input())
    list1.append(q)
print(list1)

sum1 = 0
for i in list1:
    if(i%2== 0):
        sum1=sum1+i
       
sum2 =0        
for i in list1:
    if(i%2!= 0):
        sum2=sum2+i
tuple1=(sum1,sum2)

print(tuple1)

''' output
enter no of ele :5
11
12
13
14
15
[11, 12, 13, 14, 15]
(26, 39)'''


'''Given the list list 1 = [x,y,z]
Write a list comprehension to produce the following list -
A) [x,xx,xxx,y,yy,yyy,z,zz,zzz]
B) [x,y,z,xx,yy,zz,xxx,yyy,zzz]
'''
list1 = ['x','y','z']
list2 = [lst1*num for lst1 in list1 for num in range(1,4)]
print(list2)

list3 = [lst1*num for num in range(1,4) for lst1 in list1]
print(list3)

''' output 
['x', 'xx', 'xxx', 'y', 'yy', 'yyy', 'z', 'zz', 'zzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz']
'''