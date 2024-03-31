def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return (sum/len(numbers))
    
    
c = average(1,2,3)
print(c)
        
