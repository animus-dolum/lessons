import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QCheckBox


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox1.move(20, 20)
        self.checkbox1.stateChanged.connect(self.check1)

        self.edit1 = QLineEdit(self)
        self.edit1.setText('Поле edit1')
        self.edit1.move(90, 15)
        self.edit1.resize(150, 30)

        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox2.move(20, 50)
        self.checkbox2.stateChanged.connect(self.check2)

        self.edit2 = QLineEdit(self)
        self.edit2.setText('Поле edit2')
        self.edit2.move(90, 45)
        self.edit2.resize(150, 30)

        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox3.move(20, 80)
        self.checkbox3.stateChanged.connect(self.check3)

        self.edit3 = QLineEdit(self)
        self.edit3.setText('Поле edit3')
        self.edit3.move(90, 75)
        self.edit3.resize(150, 30)

        self.checkbox4 = QCheckBox('edit4', self)
        self.checkbox4.move(20, 110)
        self.checkbox4.stateChanged.connect(self.check4)

        self.edit4 = QLineEdit(self)
        self.edit4.setText('Поле edit4')
        self.edit4.move(90, 105)
        self.edit4.resize(150, 30)

        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Прятки для виджетов')

    def check1(self, state):
        if state:
            self.edit1.show()
        else:
            self.edit1.hide()

    def check2(self, state):
        if state:
            self.edit2.show()
        else:
            self.edit2.hide()

    def check3(self, state):
        if state:
            self.edit3.show()
        else:
            self.edit3.hide()

    def check4(self, state):
        if state:
            self.edit4.show()
        else:
            self.edit4.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WidgetsHideNSeek()
    win.show()
    sys.exit(app.exec())
