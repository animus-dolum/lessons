import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 360, 46)
        self.setWindowTitle('Фокус со словами')

        self.first_value = QLineEdit(self)
        self.first_value.move(5, 10)
        self.first_value.resize(150, 30)

        self.second_value = QLineEdit(self)
        self.second_value.move(195, 10)
        self.second_value.resize(150, 30)

        self.trick_button = QPushButton(self)
        self.trick_button.setText('->')
        self.trick_button.move(160, 10)
        self.trick_button.resize(30, 30)

        self.trick_button.clicked.connect(self.run)

    def run(self):
        txt = self.first_value.text()
        if self.trick_button.text() == '->':
            self.trick_button.setText('<-')
            self.second_value.setText(self.first_value.text())
            self.first_value.setText('')
        else:
            self.trick_button.setText('->')
            self.first_value.setText(self.second_value.text())
            self.second_value.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WordTrick()
    win.show()
    sys.exit(app.exec())
