class myclass:
    def __init__(self, value):
        self.value = value 
    
    def show(self):
        print(f"Value is {self.value}")

# THIS IS GETTER USED TO GET THE VALUE WITH RETURN STATEMENT
    @property
    def ten_value(self):
        return 10 *self.value
    
# THIS IS SETTER USED TO MODIDY THE EXISTED VALUE USING FNC

    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value


a = myclass(5)
a.show()
print("This value is coming from fnc called Getters")
ten = a.ten_value
print(ten)
print("This value is coming from the fnc called Setters")
a.ten_value = 68
a.show()


