class Bell:
    def __init__(self, *args, **kwargs):
        self.ar = args
        self.kw = kwargs
        
    def print_info(self):
        kw, ar, o = dict(sorted(self.kw.items())), list(self.ar), '; '
        if ar == [] or kw == {}:
            o = ''
        if ar == [] and kw == {}:
            print('-')
        else:
            print(*', '.join([i + ': ' + kw[i] for i in kw]), o, *', '.join([*ar]), sep='')

class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        self.ar = args
        self.kw = kwargs
        self.z = 'ding'
        
    def sound(self):
        print(self.z)
        if self.z == 'ding':
            self.z = 'dong'
        else:
            self.z = 'ding'

        
class LittleBell(Bell):
    def __init__(self, *args, **kwargs):
        self.ar = args
        self.kw = kwargs
        self.z = 'ding'
        
    def sound(self):
        print(self.z)
