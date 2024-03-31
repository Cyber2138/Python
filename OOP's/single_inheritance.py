class Animal:
    def __init__(self, name, species) -> None:
        self.name = name  
        self.species = species
    
    def sound(self):
        print("This is animal sound")


class dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species = "Dog")
        self.breed = breed

    def sound(self):
        print('Bark')

a = Animal('Tiger', "Bengal")
print(a.name)

b = dog('German Shephered', 'Australian')
b.sound()