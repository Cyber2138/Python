import re

pattern = r"[A-Z]yclone"

text = '''Twinkle Twinkle little star
how i wonder what Cyclone you are
up above the world so high
like a diamond Dyclone in the sky'''

# a = re.match(pattern, text)
# print(a)

b = re.finditer(pattern, text)
for match in b:
    print(match)