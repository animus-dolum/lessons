lst = list(input())
n = int(input())
k = n if n < 0 and abs(n) < len(lst) else n % len(lst)
lst *= 2
print(''.join(list(map(lambda x: lst[lst.index(x) + k], lst[:len(lst) // 2]))))
print(''.join(lst[:len(lst) // 2]))
print(''.join(list(map(lambda x: lst[lst.index(x) - k], lst[:len(lst) // 2]))))
