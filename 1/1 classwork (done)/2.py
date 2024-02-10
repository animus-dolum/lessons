n = int(input())
c1, c2, c3, c4 = 0, 0, 0, 0
lst = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    if x > 0 and y > 0:
        c1 += 1
    elif x > 0 and y < 0:
        c4 += 1
    elif x < 0 and y > 0:
        c2 += 1
    elif x < 0 and y < 0:
        c3 += 1
    else:
        lst.append((x, y))
if lst:
    print(*lst, sep='\n')
print(f'I: {c1}, II: {c2}, III: {c3}, IV: {c4}.')
