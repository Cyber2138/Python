import time 

def Forloop():
    for i in range(50000):
        print(i)

def Whileloop():
    i = 0
    while (i<50000):
        i = i + 1
        print(i)

starting = time.time()
Forloop()
ending = time.time() - starting
starting = time.time()
Whileloop()
ending = time.time() - starting
print(starting, ending)