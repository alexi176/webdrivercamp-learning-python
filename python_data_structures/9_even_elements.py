#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
result = list()
for i in my_list:
    if i % 2 == 0:
        result.append(True)
    else:
        result.append(False)
print(my_list)
print(result)


