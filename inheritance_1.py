print("Inheritance")

class employee:
    def __init__(self,name,number):
        self.name=name
        self.number =number
        
    def details(self):
        print("name is",self.name)
        print("emp id is",self.number)
        
class manager(employee):
    def __init__(self,name,number,salary):
        super().__init__(name,number)
        self.salary = salary
    
    def mdetails(self):
        print("salary is",self.salary)
        
e1=employee("huzefa",10)
e1.details()

e2=manager("jay",20,1000)
e2.mdetails()
e2.details()