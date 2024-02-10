class BigBell:
    def __init__(self):
        self.z = 'ding'
        
    def sound(self):
        print(self.z)
        if self.z == 'ding':
            self.z = 'dong'
        else:
            self.z = 'ding'


class LittleBell:
    def __init__(self):
        self.z = 'ding'
        
    def sound(self):
        print(self.z)


class BellTower(BigBell, LittleBell):
    def __init__(self, *K):
        self.K = list(K)
        BigBell.__init__(self)
        LittleBell.__init__(self)
        
    def append(self, a):
        self.K.append(a)

    def sound(self):
        for i in self.K:
            i.sound()
        print('...')
