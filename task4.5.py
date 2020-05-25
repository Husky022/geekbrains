from functools import reduce

def function(el_1, el_2):
    return el_1 * el_2


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(function, my_list))
