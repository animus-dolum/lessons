with open('prices.txt', 'r', encoding='utf-8') as f:
    if f:
        s = str(sum(map(lambda x: float(x[-1]) * int(x[-2]), map(lambda x: x.strip().split('\t'), f.readlines()))))
        if '.' in s:
            k = len(s) - s.index('.') - 1
        else:
            k = 2
        print(s + '0' * k)
