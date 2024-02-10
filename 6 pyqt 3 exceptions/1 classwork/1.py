n = input()


def number(s):
    s = s.replace(' ', '')
    s = s.replace('\t', '')
    s = s.replace('\n', '')
    if s[:2] == '+7':
        pass
    elif s[0] == '8':
        s = '+7' + s[1:]
    else:
        return 'error'
    if '--' in s or s.count('(') != s.count(')') or s.count(')') > 1 or s[-1] == '-':
        return 'error'
    elif ')' in s:
        if s.index(')') < s.index('('):
            return 'error'
    s = s.replace('-', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    for x in s[1:]:
        if not x.isdigit():
            return 'error'
    if len(s) == 12:
        return s
    else:
        return 'error'


print(number(n))
