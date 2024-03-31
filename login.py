# creation of the id and password
print('Enter details to create your id\n')
name = input('Enter your name: ')
password = input('Enter your password: ')
print(f"Your credentials are: \n\nid = {name}\npassword = {password} ")
print('Congratulations yoru Account created Succesfully!')

# Retrival of the data
print("Enter your credentials again to login here")
id = input('Enter your id: ')
key = input('Enter your password: ')
if (id == name and key == password):
    print('Successfully login')
else:
    print('Wrong detials')

