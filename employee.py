"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, contractType,rate,commission,comRate,contractNumber):
        self.name = name
        self.contractType = contractType
        self.rate = rate
        self.commission = commission
        self.hours = 0
        self.comRate = comRate
        self.contractNumber = contractNumber   

    def add_hours(self, number):
        self.hours = number

    def get_pay(self):
        if self.contractType == "hourly":
            return (self.hours * self.rate) + self.get_commission()
        elif self.contractType == "monthly":
            return self.rate + self.get_commission()

    def get_single_pay(self):
        if self.contractType == "hourly":
            return (self.hours * self.rate)
        elif self.contractType == "monthly":
            return self.rate 

    def get_commission(self):
        if self.commission == "bonus":
            return self.comRate
        elif self.commission == "rate":
            return self.contractNumber * self.comRate
        else:
            return 0

    def __str__(self):
        statement = self.name + " works on a "

        if self.contractType == "monthly":
            statement += "monthly salary of " + str(self.get_single_pay()) 
        else:
            statement += "contract of " + str(self.hours) + " hours at " + str(self.rate) + "/hour"

        
        if self.commission == "bonus":
            statement += " and recieves a bonus commission of " + str(self.comRate)
        elif self.commission == "rate":
            statement += " and recieves a commission for " + str(self.contractNumber) + " contract(s) at " + str(self.comRate) + "/contract"


        
        statement += ". Their total pay is " + str(self.get_pay()) + "."
        return statement 


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','monthly',4000,'',0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','hourly',25,'',0,0)
charlie.add_hours(100)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','monthly',3000,'rate',200,4)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','hourly',25,'rate',220,3)
jan.add_hours(150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','monthly',2000,'bonus',1500,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','hourly',30,'bonus',600,0)
ariel.add_hours(120)