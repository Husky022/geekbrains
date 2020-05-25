from itertools import cycle

words = ["game", "player", "rules", "refery", "coach"]

i = 0
for el in cycle(words):
    if i > 15:
        break
    print(el)
    i += 1
