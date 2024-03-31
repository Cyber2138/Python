try:
    marks = [1,2,3,4,5,6,7,8,9]
    for index, marks in enumerate(marks):
        print(marks)
        if (index == 3):
            print('hey abdul')
            break
except ValueError:
     print('Something went wrong')
except TypeError:
     print('Something went wrong')