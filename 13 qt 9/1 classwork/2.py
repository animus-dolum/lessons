import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.cars = ['car2.png', 'car3.png', 'car4.png']

        self.current = 'car2.png'
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Машинка')

        self.pixmap = QPixmap(self.cars[0])
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)

        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            print(self.cars[self.current])
            self.current += 1
            self.current %= 3
            self.pixmap = QPixmap(self.cars[self.current])
            self.lbl.setPixmap(self.pixmap)
            self.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    sys.exit(app.exec_())
