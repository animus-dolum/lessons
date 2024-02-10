import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    """
    Пианино: каждая кнопка проигрывает соответствующую ноту

    Дизайн
    ------
    ui.ui - главное окно приложения

    Атрибуты
    --------
    media : list
        список URL-адресов, проигрываемых файлов mp3 (находятся в папке music)
    players : list
        список плееров под каждую ноту

    Методы
    -------
    load_mp3() :
        Подтягивает контент, создает 7 плееров под каждую ноту пианино
    ..todo:: реализовать проигрывание нот по нажатию клавиш клавиатуры
        def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.player[2].play()
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_mp3()
        self.player = QMediaPlayer()
        self.A.clicked.connect(self.players[0].play)
        self.B.clicked.connect(self.players[1].play)
        self.C.clicked.connect(self.players[2].play)
        self.D.clicked.connect(self.players[3].play)
        self.E.clicked.connect(self.players[4].play)
        self.F.clicked.connect(self.players[5].play)
        self.G.clicked.connect(self.players[6].play)

    def load_mp3(self):
        media = [QUrl.fromLocalFile('music/A.mp3'), QUrl.fromLocalFile('music/B.mp3'),
                 QUrl.fromLocalFile('music/C.mp3'), QUrl.fromLocalFile('music/D.mp3'),
                 QUrl.fromLocalFile('music/E.mp3'), QUrl.fromLocalFile('music/F.mp3'),
                 QUrl.fromLocalFile('music/G.mp3')]
        content = [QMediaContent(i) for i in media]
        self.players = [QMediaPlayer() for _ in content]
        for i in range(len(content)):
            self.players[i].setMedia(content[i])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())