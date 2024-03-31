#  THIS IS THE WAY TO WRITE INTO ANY FILE 

f = open('file.txt','w')
f.write('''twinkle twinkle little star 
how I wonder what you are
up above the world so high
like a diamond in the sky!!!''')
f.close()

# THIS IS THE WAY TO READ ANY FILE

f = open('file.txt','r')
t = f.read()
f.close()
# print(t)

# (THIS IS ANOTHER METHOD TO READ THE FILE)

with open('file.txt','r') as f:
    t = f.read()
    print(t)

f = open('file.txt','r')

for i in f:
    t = f.readlines()
    if not t:
        break
    print(t)

while True:
    line = f.readlines()
    if not line:
        break
    print(line)

# THIS IS THE WAY TO APPEND THE NEW TEXTUAL DATA TO THE EXISTING FILE

f = open('file.txt','a')
f.write('\nThis is Abdul here hope you guys are doing well')
f.close()