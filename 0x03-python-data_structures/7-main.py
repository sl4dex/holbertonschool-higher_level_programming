#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (2,3)
tuple_b = (2, 3)
new_tuple = add_tuple(tuple_a, tuple_b)#4, 6
print(new_tuple)

print(add_tuple(tuple_a, ()))#2, 3
print(add_tuple(tuple_a, (1, )))#3, 3
print(add_tuple((1, ), tuple_b))#3, 3
print(add_tuple((1, ), (2, )))#3, 0
print(add_tuple((), tuple_b))#2, 3
