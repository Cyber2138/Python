print("welcome to KBC\n")
correct  = 'Congratulation you give the correct answer'
wrong = 'You choose the wrong answer!!'

question1 = '1)Who invented "0"?  \n'
print(question1)
option1 = ['1) Aryabhatta','2) Albert Einstine','3) Euclid','4) Newton']
for i in option1:
    print(i,'\n')
key = [1,2,3,4]
reply = int(input('Enter your answer: '))
if (reply == key[0]):
    print('\n',correct.upper())
else:
    print(wrong.upper())

question2 = '\n2)How many moons does the planet Earth have? \n'
print(question2)
option2 = ['1) 3','2) 2','3) 1','4) 4']
for i in option2:
    print(i,'\n')
reply = int(input('Enter your answer: '))
if (reply == key[2]):
    print('\n',correct.upper())
else:
    print(wrong.upper())
    
question3 = '\n3)How much legs does the octopus have? \n'
print(question3)
option3 = ['1) 7','2) 9','3) 10','4) 8']
for i in option3:
    print(i,'\n')
reply = int(input('Enter your answer: '))
if (reply == key[3]):
    print('\n',correct.upper())
else:
    print(wrong.upper())

question4 = '\n4)Pingu me sea lion ka name kya rehta? \n'
print(question4)
option4 = ['1) Pingu','2) Dhaibada','3) Kharibundi','4) bambal machi']
for i in option4:
    print(i,'\n')
reply = int(input('Enter your answer: '))
if (reply == key[1]):
    print('\n',correct.upper())
else:
    print(wrong.upper())

question5 = '\n4)Bandar phoda kisku bolte? \n'
print(question5)
option5 = ['1) Phunsi','2) Dumbal','3) Daat','4) Dadoda']
for i in option5:
    print(i,'\n')
reply = int(input('Enter your answer: '))
if (reply == key[3]):
    print('\n',correct.upper())
else:
    print(wrong.upper())


