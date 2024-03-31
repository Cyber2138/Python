greeting = 'the number you entered it will generate the table of it'
print(greeting.upper())
print('YOUR TABLE WOULD BE LIKE')
try:
    a = int(input('Enter you number: '))
    for i in range(1,11):
        print(f'{a} X {i} = {int(a*i)}')
except ValueError:
    print('Invalid input!!')

print('This will show you the square root of the entered number')
try:
    num = int(input('Enter the number you want: '))
    root = num**2
    print(root)
except ValueError:
    print('you entered the wrong input')

