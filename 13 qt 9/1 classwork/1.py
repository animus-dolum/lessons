from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
import random

SCREEN_SIZE = [1000, 1000]


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.figure = 'triangle'
        self.flag = False
        self.color = (0, 0, 0)
        self.x, self.y = 0, 0
        self.coords = []
        self.sizee = 0

        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Супрематизм')
        self.flag = False

    def draw(self):
        self.sizee = random.randint(10, 100)
        self.color = QColor(*[random.randint(0, 255) for _ in 'abc'])
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(0, 0, 0))
            qp.setBrush(QColor(self.color))
            if self.figure == 'square':
                qp.drawRect(self.x - self.sizee // 2, self.y - self.sizee // 2, self.sizee, self.sizee)
            elif self.figure == 'circle':
                qp.drawEllipse(self.x - self.sizee // 2, self.y - self.sizee // 2, self.sizee, self.sizee)
            elif self.figure == 'triangle':
                self.drawTriangle(qp)
            qp.end()

    def drawTriangle(self, qp):
        a = self.x, self.y - self.sizee * 2
        b = self.x + int(3 * self.sizee / 3 ** 0.5), self.y + self.sizee
        c = self.x - int(3 * self.sizee / 3 ** 0.5), self.y + self.sizee
        points = [QPoint(a[0], a[1]), QPoint(b[0], b[1]), QPoint(c[0], c[1])]
        qp.drawPolygon(QPolygon(points))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.figure = 'triangle'
            self.draw()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.figure = 'circle'
            self.draw()
        elif event.button() == Qt.RightButton:
            self.figure = 'square'
            self.draw()

    def mouseMoveEvent(self, event):
        self.x, self.y = int(event.x()), int(event.y())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())
