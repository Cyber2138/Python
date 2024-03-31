a = input('Enter the number between 1 to 10: ')

if (str(a)=='quit'):
    print('The program is successfully ended')
elif (int(a)<0 or int(a)>10):
    print(a)
    raise ValueError ('The number you entered is not matching the given criteria')
