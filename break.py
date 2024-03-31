num = int(input('Enter the number you wanna generate table of: '))
for i in range(20):
    if (i==10):
        break
    print(num,'X', i ,'=', num * i)