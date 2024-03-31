#  THIS IS PUBLIC ACCESS MODIFIER
class employee:
    def __init__(self):
        self.name = 'Abdul'
        self.age = 23

a = employee()
print(a.name)

# THIS IS PRIVATE ACCESS MODIFIER
class emp:
    def __init__(self):
        self.__name = 'Mohammed'
        self.__age = 25

b = emp()
print(b._emp__name)

# THIS IS PROTECTED ACCESS MODIFIER
class details(emp):
    def __init__(self):
        self._name = 'Rahman'
        self._age = 21
    
    def _greet():
        return "Hello World"

c = details
print(c._greet())
        
