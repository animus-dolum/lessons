N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    dct = dict(zip(PITCHES, LONG_PITCHES))

    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return Note.dct[self.note]
        else:
            return self.note

    def __lt__(self, y):
        return PITCHES.index(self.note) < PITCHES.index(y)

    def __le__(self, y):
        return PITCHES.index(self.note) <= PITCHES.index(y)

    def __eq__(self, y):
        return self.note == y

    def __rshift__(self, n):
        k = n if n < 0 and abs(n) < len(PITCHES) else n % len(PITCHES)
        return Note((PITCHES * 2)[PITCHES.index(self.note) + k], self.is_long)

    def __lshift__(self, n):
        k = n if n < 0 and abs(n) < len(PITCHES) else n % len(PITCHES)
        return Note((PITCHES * 2)[PITCHES.index(self.note) - k], self.is_long)

    def get_interval(self, other):
        x, y = PITCHES.index(other), PITCHES.index(self.note)
        return INTERVALS[max(x, y) - min(x, y)]


class Melody:
    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self.lst = lst

    def __str__(self):
        return ', '.join(map(lambda x: str(x), list(self.lst))).capitalize()

    def __repr__(self):
        return ', '.join(map(lambda x: str(x), self.lst)).capitalize()

    def append(self, x):
        self.lst.append(x)

    def replace_last(self, x):
        self.lst[-1] = x

    def remove_last(self):
        self.lst = self.lst[:-1]

    def clear(self):
        self.lst = []

    def __len__(self):
        return len(self.lst)

    def __rshift__(self, n):
        f = 1
        for x in self.lst:
            if x >> n <= x:
                f = 0
        if f:
            return Melody(list(map(lambda x: x >> n, self.lst)))
        else:
            return Melody(self.lst.copy())

    def __lshift__(self, n):
        f = 1
        for x in self.lst:
            if x << n >= x:
                f = 0
        if f:
            return Melody(list(map(lambda x: x << n, self.lst)))
        else:
            return Melody(self.lst.copy())


melody = Melody([Note('ля'), Note('соль'), Note('ми'),  Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)
