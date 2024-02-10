import sys
import io


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout


template = '''
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>90</y>
      <width>371</width>
      <height>371</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="widgetArt"/>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''.strip()


class WidgetArt(QMainWindow):
    def __init__(self, mtrx):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.mtrx = mtrx

        self.run()

    def run(self):
        grid = QGridLayout(self)

        for i in range(len(self.mtrx)):
            for j in range(len(self.mtrx[i])):
                button = QPushButton(self)
                button.setText('*' if self.mtrx[i][j] else '')
                button.resize(50, 50)
                grid.addWidget(button, 50 * (i + 1), 50 * (j + 1))

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    matrix = [
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    ]
    ex = WidgetArt(matrix)
    ex.setFixedSize(500, 800)
    ex.setWindowTitle('Form')
    ex.show()
    sys.exit(app.exec_())
