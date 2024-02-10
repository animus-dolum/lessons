import sys
from PyQt5.QtWidgets import *


class MiniCalcularor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Миникалькулятор')

        self.name_label = QLabel(self)
        self.name_label.setText("Первое число(целое): ")
        self.name_label.move(5, 20)

        self.number_1 = QLineEdit(self)
        self.number_1.move(5, 50)
        self.number_1.resize(150, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Второе число(целое): ")
        self.name_label.move(5, 90)

        self.number_2 = QLineEdit(self)
        self.number_2.move(5, 120)
        self.number_2.resize(150, 30)

        self.calculate_button = QPushButton(self)
        self.calculate_button.setText('->')
        self.calculate_button.move(160, 85)
        self.calculate_button.resize(80, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Сумма: ")
        self.name_label.move(300, 20)

        self.result_sum = QLCDNumber(self)
        self.result_sum.move(350, 15)

        self.name_label = QLabel(self)
        self.name_label.setText("Разность: ")
        self.name_label.move(280, 50)

        self.result_sub = QLCDNumber(self)
        self.result_sub.move(350, 45)

        self.name_label = QLabel(self)
        self.name_label.setText("Произведение: ")
        self.name_label.move(260, 80)

        self.result_mul = QLCDNumber(self)
        self.result_mul.move(350, 75)

        self.name_label = QLabel(self)
        self.name_label.setText("Частное: ")
        self.name_label.move(290, 110)

        self.result_div = QLCDNumber(self)
        self.result_div.move(350, 105)

        self.count = 0

        self.calculate_button.clicked.connect(self.run)

    def run(self):
        number_1 = self.number_1.text()
        number_2 = self.number_2.text()

        self.result_sum.display(str(int(number_1) + int(number_2)))
        self.result_sub.display(str(int(number_1) - int(number_2)))
        self.result_mul.display(str(int(number_1) * int(number_2)))
        if number_2 == '0':
            txt = 'Error'
        else:
            txt = str(round(int(number_1) / int(number_2), 3))
        self.result_div.display(txt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MiniCalcularor()
    win.show()
    sys.exit(app.exec())
