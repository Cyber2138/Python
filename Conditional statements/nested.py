print('this program will find the number you are entered in!!')
num = int(input('Enter the number: '))
if (num<0):
    print(num, 'is less than "0"')
elif (num>0):
    if (num<=9):
        print('your num is in between than "0-10"')
    elif(num<=19):
        print('your num is in between "10-20"')
    elif(num<=29):
        print('your num is in between "20-30"')
    elif(num<=39):
        print('your num is in between "30-40"')
    elif(num<=49):
        print('your num is in between "40-50"')
    elif(num<=59):
        print('your num is in between "50-60"')
    elif(num<=69):
        print('your num is in between "60-70"')
    elif(num<=79): 
        print('your num is in between "70-80"')
    elif(num<=89):
        print('your num is in between "80-90"')
    elif(num<=99):
        print('your num is in between "90-100"')
else:
    print('your num is greater than 100')



    

