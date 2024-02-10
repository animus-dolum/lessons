import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.button.clicked.connect(self.run)

    def run(self):
        name = self.filenameEdit.text()

        try:
            with open(name, 'r', encoding='utf-8') as f:
                data = f.readlines()
            if data:
                print(data)
                data = [int(x.strip()) for x in data]
                print(data)
                #self.text_field.setText(random.choice(data))
            raise TypeError
        except FileNotFoundError:
            self.statusBar().showMessage('Error')
        except ValueError:
            self.statusBar().showMessage('Error2')
        except TypeError:
            self.statusBar().showMessage('Error1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.setFixedSize(500, 500)
    ex.setWindowTitle('Случайная строка')
    ex.show()
    sys.exit(app.exec_())
