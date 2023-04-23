from abc import ABC , abstractmethod

class banking(ABC):
    @abstractmethod
    def calculate():
        pass

    @abstractmethod
    def update():
        pass
    
class customer(banking):
    def __init__(self, acctype, bal):
        self.acc = acctype
        self.bal = bal
        self.irate = 0

        if(self.acc == "saving"):
            self.irate = 4/100
        elif(self.acc == "current"):
            self.irate = 6/100
        else:
            print("Undefined acc type")

    def calculate(self):
        self.interest = self.bal*self.irate
        print(f"Current Interest : {self.interest}")

    def update(self):
        if(self.bal > 100000):
            self.bal += self.bal*5/100
            print(f"Your Updated Balance is : {self.bal}")
        else:
            print("Acc balance too low")


class employee(banking):
    def __init__(self, emptype, wtime):
        self.emptype = emptype
        self.wtime = wtime
        self.gsal = 0
        self.bsal = 0

        if(self.emptype == "class1"):
            self.bsal = 30000
            self.da = self.bsal*121/100
        elif(self.emptype == "class2"):
            self.bsal = 20000
            self.da = self.bsal*115/100
        else:
            print("Undefined employee type")

        self.hra = self.bsal*30/100

    def calculate(self):
        self.gsal = self.bsal + self.da + self.hra
        print(f"Your Gross salary is : {self.gsal}")

    def update(self):
        if(self.wtime > 15):
            self.gsal += self.gsal*20/100
            print(f"Your Salary with Bonus is : {self.gsal}")
        else:
            print("You have worked too less")

c1 = customer("saving", 1000)
c2 = customer("current", 1000000000)
e1 = employee("class1", 10)
e2 = employee("class2", 20)

c1.calculate()
c2.calculate()
e1.calculate()
e2.calculate()

c1.update()
c2.update()
e1.update()
e2.update()