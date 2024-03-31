class person:
    def __init__(self, name, occ):
        # print("Hi this is your assistant")
        self.name = name
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Abdul Rahman", "Data Scientist")
b = person("Abdul Raheem","Quality Analyst")
a.info()
b.info()

