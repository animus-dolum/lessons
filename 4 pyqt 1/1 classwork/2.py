import sys
from PyQt5.QtWidgets import *


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Вычиление выражений')

        self.name_label = QLabel(self)
        self.name_label.setText("Выражение: ")
        self.name_label.move(5, 20)
        self.name_label = QLabel(self)
        self.name_label.setText("Результат: ")
        self.name_label.move(195, 20)

        self.first_value = QLineEdit(self)
        self.first_value.move(5, 50)
        self.first_value.resize(150, 30)

        self.second_value = QLineEdit(self)
        self.second_value.move(195, 50)
        self.second_value.resize(150, 30)

        self.trick_button = QPushButton(self)
        self.trick_button.setText('->')
        self.trick_button.move(160, 50)
        self.trick_button.resize(30, 30)

        self.trick_button.clicked.connect(self.run)

    def run(self):
        txt = self.first_value.text()
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Evaluator()
    win.show()
    sys.exit(app.exec())
