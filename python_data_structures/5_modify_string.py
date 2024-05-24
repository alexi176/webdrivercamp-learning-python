#!/usr/bin/python3
string = """AbraCadabra
A new string voila!"""
new_string = ''
for i in string:
    if i != 'a' and i != 'A':
        new_string += i
    else:
        continue
print(new_string)
