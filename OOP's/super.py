class Employee:
    def __init__(self, name , age) -> None:
        self.name = name 
        self.age = age

class programmer(Employee):
    def __init__(self, name, age, lang) -> None:
        super().__init__(name, age)
        self.lang = lang

a = Employee('Abdul',20)
b = programmer("Mohammed", 23, 'python')
print(b.name, b.age, b.lang)