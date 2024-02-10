lst = input().split(' -> ')

n = int(input())
for _ in range(n):
    s = input()
    if lst.index(s) == 0:
        print(' -> '.join(lst[:2]))
    elif s == lst[-1]:
        print(' -> '.join(lst[-2:]))
    else:
        print(' -> '.join(lst[lst.index(s) - 1:lst.index(s) + 2]))
