print("Function in python")

def numbers(a,b):
    print(a,b)
    add(a,b)
    sub(a,b)
    r1=mul(a,b)
    print(r1(10,20))
    div(a,b)
    
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)
    
def mul(a,b):
   return lambda a,b : a*b
    
def div(a,b):
    print(a/b)
    
numbers(10,20)