class Employee:
    def __init__(self, name) -> None:
        self.name = name 

    def info(self):
        print(self.name)

class dancer:    
    def __init__(self, dance) -> None:
        self.dance = dance

    def info(self):
        print(self.dance)

class DancerEmployee(Employee, dancer):
    def __init__(self, name, dance) -> None:
        super().__init__(name)
        self.name = name
        self.dance = dance

a = DancerEmployee("Jhummo", "Marfa")
print(DancerEmployee.mro())

