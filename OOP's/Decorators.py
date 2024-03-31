def greet(fx):
    def Mfx(*args, **kwargs):
         print("Good Morning")
         fx(*args, **kwargs)
         print("Thanks for using this Fnc")
    return Mfx


@greet
def hello():
     print('Hello World')

hello()

@greet
def add(a,b):
     add = a+b
     print(f"The sum of the two number is {add}")
add(5,5)