from random import choice


with open('lines.txt', 'r') as f:
    try:
        print(choice(f.readlines()))
    except IndexError:
        pass