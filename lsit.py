fruits = ['Apple','mango','grapes','orange',1,2,3]
print(fruits)

if "apple" in fruits:
    print('Yes')
else:
    print('No')

for i in fruits:
    print(i)

basket = fruits.copy()
basket.insert(0,'pine apple')
basket.append([4,5])
print(basket.count('apple'))
print(basket.remove('Apple'))
print(basket)