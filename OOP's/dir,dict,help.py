# THIS SHOWS HOW THE DIR METHOD WORKS
l = [1,2,3,4,5,6]
print(dir(l))


# THIS SHOWS HOW __DICT__ ATTRIBUTE WORKS
class person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age

a = person('Abdul', 20)
print(a.__dict__)

# THIS SHOWS HOW THE HELP KEYWORD WORKS
print(help(person))