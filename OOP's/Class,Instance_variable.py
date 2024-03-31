# THIS CAN SHOWS THE DIFFERENCES OF THE CLASS VARIABLES AND THE INSTANCES VARIABLES

class employee:
    company = 'Apple' #this is the class variable
    def __init__(self, name):
        self.name = name 
        self.raiseamt = 20

    def info(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raiseamt}\nHe worked in {self.company}")    

a = employee('Abdul')
a.raiseamt = 100
a.info()
