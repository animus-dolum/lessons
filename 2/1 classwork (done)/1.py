class Note:
    def __init__(self, s):
        self.s = s

    def play(self):
        print(self.s)


do = Note("до")
sol = Note("соль")
sol.play()
do.play()
