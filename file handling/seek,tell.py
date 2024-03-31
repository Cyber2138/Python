with open('file.txt', 'r') as f:
    f.seek(15)
    position = f.tell()
    print(position)
    text = f.read(10)
    print(text)