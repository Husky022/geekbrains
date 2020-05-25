from itertools import count

def function(start_number, max_number):

    for i in count(start_number):
        if i > max_number:
            break
        else:
            print(i)


function(int(input('Введите начальное число ')), int(input('Введите конечное число ')))
