lst = ['камень', 'ножницы', 'бумага'] * 2
s1, s2 = input(), input()
if s2 == lst[lst.index(s1) + 1]:
    print('первый')
elif s1 == lst[lst.index(s2) + 1]:
    print('второй')
else:
    print('ничья')
