#WAP to print a star pattern.
n = int(input("Enter a number"))
for i in range(0,n):
    for j in range (i):
        print('*', end =" ")
    print(" ")  
for i in range(n,0,-1):
    for j in range (i):
        print('*', end =" ")
    print(" ") 
''' output
Enter a number 5
 
*  
* *  
* * *  
* * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
'''



#WAP to accept name and surname in two variables and print them in reverse.
f = input("Enter a Fname ")
l = input("Enter a Lname ")    
print(f , l)
a=len(f)
b=len(l)
for i in range(len(l)-1,-1,-1):
    print(l[i], end="")
   
   
for i in range(len(f)-1,-1,-1):
    print(f[i], end="")

''' output
Enter a Fname huzefa
Enter a Lname dohadwala
huzefa dohadwala
alawdahod afezuh'''

