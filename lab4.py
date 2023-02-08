''' WAP to add n number of int using function'''
def add_number(args):
#function for sum of n numbers
    sum1=0
    for i in args:
        sum1=sum1+i
    print("sum=" , sum1)
l1 =[]
print("Enter number of ele")
ele= int(input())

for j in range (ele):
    n=int(input())
    l1.append(n)
add_number(l1)

''' output
Enter number of ele
5
10
20
30
40
50
sum= 150
'''

'''For a given seq of n values x1,x2..... , a window of size k>0
k=n-k+1 '''
l2=[3,5,7,2,8,10,11,65,72,81,99,100,150]
k=3
outval=len(l2)-k+1
print("number of output value",outval)
for i in range(outval):
    avg=0
    sum2=0
    for j in l2:
        sum2=sum(l2[i:i+k])
        avg=sum2/k
    print(avg)    
''' output
number of output value 11
5.0
4.666666666666667
5.666666666666667
6.666666666666667
9.666666666666666
28.666666666666668
49.333333333333336
72.66666666666667
84.0
93.33333333333333
116.33333333333333
'''