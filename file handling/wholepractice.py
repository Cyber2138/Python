# STRING METHODS

print('hello world')
a = "Hi this is planet Earth"
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.count('i'))
print(a.endswith('Earth'))
print("this shows the find in the given statement",a.find('this'))


# LOOPING METHODS

# FOR LOOP 
print('this is for loop')
for i in range(100):
    print(i)
    if i == 50:
        break

# WHILE LOOP
a = 0
print('this is while loop')
while (a<100):
    print(a)
    a = a + 1
    if a == 70:
        break

# USER DEF FUNCTION 
def sum(a,b):
    sum = a+b
    print('The sum of the two numbers are: ',sum )
sum(5,5)


add = lambda x:x+x
print('the sum of the given number of its twice is ',add(8))
   
subtract = lambda a,b:a-b
print('the subtraction of the same number is: ',subtract(100,50))


# LISTING METHODS
names = ['apple','orange','mango','grapes']
for i in names:
    print(i) 
# names.sort() 
names.reverse() 
names.count('apple') 
names.append('pine apple')
print(names)


num = [1,2,8,5,3]
num.sort()
print(num)


if 'apple' in names:
    print('Yes it have apple in your list')
else:
    print("No you don't have apple in your list")