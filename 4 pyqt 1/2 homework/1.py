import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.first_value = QLineEdit(self)
        self.first_value.setText('0')
        self.first_value.move(10, 10)
        self.first_value.resize(30, 30)

        self.add_button = QPushButton(self)
        self.add_button.setText('+')
        self.add_button.move(50, 10)
        self.add_button.resize(30, 30)
        self.add_button.clicked.connect(self.add)

        self.substract_button = QPushButton(self)
        self.substract_button.setText('-')
        self.substract_button.move(90, 10)
        self.substract_button.resize(30, 30)
        self.substract_button.clicked.connect(self.substract)

        self.multiply_button = QPushButton(self)
        self.multiply_button.setText('*')
        self.multiply_button.move(130, 10)
        self.multiply_button.resize(30, 30)
        self.multiply_button.clicked.connect(self.multiply)

        self.second_value = QLineEdit(self)
        self.second_value.setText('0')
        self.second_value.move(170, 10)
        self.second_value.resize(30, 30)

        self.eq = QLabel(self)
        self.eq.setText('=')
        self.eq.move(210, 10)
        self.eq.resize(30, 30)

        self.result = QLineEdit(self)
        self.result.setText('0')
        self.result.move(230, 10)
        self.result.resize(30, 30)
        self.result.setEnabled(False)

    def add(self):
        self.result.setText(str(int(self.first_value.text()) + int(self.second_value.text())))

    def substract(self):
        self.result.setText(str(int(self.first_value.text()) - int(self.second_value.text())))

    def multiply(self):
        self.result.setText(str(int(self.first_value.text()) * int(self.second_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.setFixedSize(300, 100)
    ex.show()
    sys.exit(app.exec_())
