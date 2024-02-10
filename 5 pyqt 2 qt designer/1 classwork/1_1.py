import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

import math


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)

        self.expr = ''

        self.res = ''

        self.res = ''

        self.f = 1

        for button in self.buttonGroup_digits.buttons():
            button.clicked.connect(self.num)

        for button in self.buttonGroup_binary.buttons():
            button.clicked.connect(self.operation)

        self.btn_clear.clicked.connect(self.clear)

        self.btn_eq.clicked.connect(self.eq)

        self.btn_dot.clicked.connect(self.num)

        self.btn_fact.clicked.connect(self.fact)

        self.btn_sqrt.clicked.connect(self.sqrt)

    def num(self):
        self.res += self.sender().text()

        self.run()

    def operation(self):
        self.expr += self.res + self.sender().text()
        self.f = 0

        self.run()

        self.res = ''

    def fact(self):
        try:
            self.res = str(math.factorial(int(self.res)))
        except Exception:
            self.res = 'Error'

        self.run()

    def sqrt(self):
        try:
            self.expr = str(math.sqrt(int(float(self.res))))
            self.res = self.expr
        except Exception:
            self.res = 'Error'

        self.run()

    def clear(self):
        self.expr = ''
        self.res = ''

        self.run()

    def eq(self):
        self.expr += self.res
        self.res = str(eval(str(self.expr).replace('^', '**')))

        self.run()

        self.expr = self.res
        self.f = 1

    def run(self):
        self.table.display(self.res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
