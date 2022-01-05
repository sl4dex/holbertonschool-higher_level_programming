#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        total, divisor = 0, 0
        for x, y in my_list:
            total += x * y
        for i in range(len(my_list)):
            divisor += my_list[i][1]
        return total / divisor
