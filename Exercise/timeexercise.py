import time
t = time.strftime('%H, %M, %S')
hour = time.strftime("%H")
hour = input('Enter the hour: ')
hour = int(hour)
print(hour)
if (hour>=0 and hour<12):
    print('Good morning sir!')
elif (hour>=12 and hour<17):
    print('Good afternoon sir!')
elif (hour>=17 and hour<24):
    print('Good night sir!')
else:
    print('Invalid input')
