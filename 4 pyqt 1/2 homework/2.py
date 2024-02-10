import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        alphabet_buttons = {
            'a': QPushButton(self),
            'b': QPushButton(self),
            'c': QPushButton(self),
            'd': QPushButton(self),
            'e': QPushButton(self),
            'g': QPushButton(self),
            'h': QPushButton(self),
            'i': QPushButton(self),
            'j': QPushButton(self),
            'k': QPushButton(self),
            'l': QPushButton(self),
            'm': QPushButton(self),
            'n': QPushButton(self),
            'o': QPushButton(self),
            'p': QPushButton(self),
            'q': QPushButton(self),
            'r': QPushButton(self),
            's': QPushButton(self),
            't': QPushButton(self),
            'u': QPushButton(self),
            'v': QPushButton(self),
            'w': QPushButton(self),
            'x': QPushButton(self),
            'y': QPushButton(self),
            'z': QPushButton(self)
        }

    def initUI(self):
        self.result = QLineEdit(self)
        self.result.setText('0')
        self.result.move(20, 100)
        self.result.resize(300, 50)
        self.result.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.setFixedSize(400, 200)
    ex.show()
    sys.exit(app.exec_())
