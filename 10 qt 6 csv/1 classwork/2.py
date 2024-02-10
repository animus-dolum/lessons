from csv import reader


with open('wares.csv', 'r', encoding='utf-8') as f:
    reader = reader(f, delimiter=';', quotechar='"')
    lst = list(sorted(reader, key=lambda x: int(x[-1])))
    ans = []
    m = 1000
    for elem in lst:
        name, cost = elem[0], int(elem[1])
        for x in range(m // cost):
            if name in ans:
                if ans.count(name) >= 10:
                    break
            ans.append(name)
            m -= cost
    if ans:
        print(*ans, sep=', ')
    else:
        print('error')
