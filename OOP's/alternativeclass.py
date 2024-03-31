class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name  
        self.salary = salary

    @classmethod
    def change(cls, string):
        change = cls(string.split(',')[0], string.split(',')[1])
        return change

    def info(self):
        print(f"The name of the emp is {self.name} and his salary is {self.salary}")

string = "Ahmed,9000"
a = Employee('Abdul', 50000)
a.info()
b = Employee.change(string)
b.info()