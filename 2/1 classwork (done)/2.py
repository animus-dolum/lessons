class Note:
    def __init__(self, s, f=False):
        self.s = s
        self.f = f

    def play(self):
        print(self.s)

    def __str__(self):
        if self.f:
            lst = ['до-о', 'ре-э', 'ми-и', 'фа-а', 'со-оль', 'ля-а', 'си-и']
            return lst[list(map(lambda x: x[:2], lst)).index(self.s[:2])]
        else:
            return self.s


sool = Note("соль", True)
laa = Note("ля", True)
print(sool, laa)
