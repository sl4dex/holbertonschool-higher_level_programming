#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
new_list = delete_at(my_list, 9)
print(new_list)
print(my_list)
new_list = delete_at(my_list, -3)
print(new_list)
print(my_list)
