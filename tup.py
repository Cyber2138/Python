random = (1,2,3,4,5,6, 'Tiger','Lion')
print(type(random), random)
if 'Tiger' in random:
    print('Yes it is present in the tuple')

country = ('Spain', 'India', 'England', 'Russia')
temp = list(country)
temp.append('Turkey')
print(temp)
temp.pop(3)
print(temp)
country = tuple(temp)
print(country)