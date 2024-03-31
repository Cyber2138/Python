def gum():
    for i in range(100):
        yield i
gen = gum()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))