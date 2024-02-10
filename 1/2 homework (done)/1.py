lst1 = ['ножницы', 'бумага', 'камень', 'ром', 'пират'] * 2
lst2 = ['ножницы', 'ром', 'бумага', 'пират', 'камень'] * 2

s1, s2 = input(), input()
if s2 == lst1[lst1.index(s1) + 1] or s2 == lst2[lst2.index(s1) + 1]:
    print('первый')
elif s1 == lst1[lst1.index(s2) + 1] or s1 == lst2[lst2.index(s2) + 1]:
    print('второй')
else:
    print('ничья')
