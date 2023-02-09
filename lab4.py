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
l2 =[]
k=0
outval=0

print("Enter number of ele")
ele= int(input())
print("Enter values:")

for j in range (ele):
    n=int(input())
    l2.append(n)
     
print("Enter value of K:")
k=int(input())
outval=len(l2)-k+1
print("Output value=",outval)
    
def avg (args):
    for i in range(outval):
        avg=0
        sum2=0
        for j in args:
            sum2=sum(l2[i:i+k])
            avg=sum2/k
        print(round(avg,3))    
     
avg(l2) 
  
''' output
Enter number of ele:
13
Enter values:
3
5
7
2
8
10
11
65
72
81
99
100
150
Enter value of K:
3
Output value= 11
5.0
4.667
5.667
6.667
9.667
28.667
49.333
72.667
84.0
93.333
116.333'''