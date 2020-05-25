from itertools import count, cycle

def function(max_number):
    for i in count(1):
        if i > max_number:
            break
        else:
            print(next(el))


words = ["game", "player", "rules", "refery", "coach"]
el = cycle(words)

function(int(input('Введите конечное число ')))
