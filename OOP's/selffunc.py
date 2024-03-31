class person:
    name = "Abdul"
    age = 10
    occupation = "Data Analyst"
    def info(self):
        print(f"{self.name}, is a {self.occupation}")
# print(person.name, person.age, person.occupation)

a = person()
a.name = "Mohammed Abdul Rahman"
a.age = 23
a.occupation = 'Data Scientist'
# print(f"{a.name} his age is {a.age} and he is a {a.occupation}")
a.info()

b = person()
b.name = "Mohammed Abdul Raheem"
b.age = 22
b.occupation = "Devops Engineer"
b.info()