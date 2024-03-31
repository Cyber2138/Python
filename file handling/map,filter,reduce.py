def cube(x):
    return x*x*x
print(cube(2))

l = [1,2,3,4,5,6,7,8,9]
newlist = []
for item in l:
    newlist.append(cube(item))
    print(newlist)

# MAP FUNCTION

newl = list(map(cube,l))
print(newl)

# FILTER FUNCTION

def filter_function(a):
    return a>2
    
newll = list(filter(filter_function,l))
print('This shows the numbers filtered by the expression using filter funciton',newll)


# REDUCE FUNCTION

from functools import reduce
a = [2,3,4,5,6]
def mysum(x,y):
    return x+y
sum = reduce(mysum,a)
print('This shows the items of the list can adding each other and shows the aggregate output as a result',sum)

add = reduce(lambda x,y : x+y, a)
print('This shows the same results by using lambda function: ',add)