PITCHES = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']


class Note:
    dct = {'до': 'до-о',
           'ре': 'ре-э',
           'ми': 'ми-и',
           'фа': 'фа-а',
           'соль': 'со-оль',
           'ля': 'ля-а',
           'си': 'си-и'
           }

    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return Note.dct[self.note]
        else:
            return self.note


class LoudNote(Note):
    def __str__(self):
        if self.is_long:
            return Note.dct[self.note].upper()
        else:
            return self.note.upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=False):
        self.note = note
        self.is_long = is_long


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        self.note = note
        self.octave = octave
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return f'{Note.dct[self.note]} ({self.octave})'
        else:
            return f'{self.note} ({self.octave})'


print(Note("соль"))

print(LoudNote(PITCHES[4]))
print(LoudNote("си", is_long=True))

print(DefaultNote("ми"))
print(DefaultNote())
print(DefaultNote(is_long=True))

print(NoteWithOctave("ре", "первая октава"))
print(NoteWithOctave("ля", "малая октава", is_long=True))