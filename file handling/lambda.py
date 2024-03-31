def sum(a,b):
    sum = a+b
    print('The sum of the two numbers are: ', sum)
sum(5,6)

add = lambda x: x+x
print('The print of the two numbers using lambda fnc is: ',add(5))

# THIS IS THE DOUBLE FUNCTION WHICH RETURNS THE VALUE MULTIPLIED BY 2

def double(x):
    double = x*2
    print('The double value of the number you entered is: ', double)
double(5)

dubble = lambda x:x*2
a = dubble(2)
print('The double value of the varaible using lambda function is: ',a)