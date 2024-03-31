class employee:
    def __init__(self, name, id, address):
        self.name = name 
        self.id = id 
        self.address = address 

    def show(self):
        print(f"The employee of {self.id} is {self.name}")

# Here we apply the inheritance method to use this class for further operations 
class manager(employee):
    def language(self):
        print("The language is Python")

a = employee("Abdul", 5400, "kalapather")
b = employee("samad",6500,"Somajiguda")
c = manager("Ahmed", 8000, "Gachibowli")
h = manahr()
a.show()
b.show()
c.show()
h.language()