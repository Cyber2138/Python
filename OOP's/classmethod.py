class Employee:
    company = "Apple"
    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def changecompany(cls, comp):
        cls.company = comp
    

    def info(self):
        print(f"The name of the Employee is{self.name} and worked in {self.company}")

a = Employee('Abdul')
a.company = "Tesla"
a.info()
print(Employee.company)
a.changecompany('Tesla')
print(Employee.company)