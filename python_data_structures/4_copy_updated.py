#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
modified_list = list_.copy()

for i in range(len(list_)):
    if list_[index] == 4:
        list_[i] = element_to_replace
print('Copy:',list_)
print('Original:',modified_list)
