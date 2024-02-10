import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import choice


template = '''
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>468</width>
    <height>325</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>90</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Получить</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="text_field">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>100</y>
      <width>231</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>180</y>
      <width>371</width>
      <height>61</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>468</width>
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


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.button.clicked.connect(self.run)

    def run(self):
        with open('lines.txt', 'r', encoding='utf-8') as f:
            try:
                self.text_field.setText(choice(f.readlines()))
            except IndexError:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.setFixedSize(500, 500)
    ex.setWindowTitle('Случайная строка')
    ex.show()
    sys.exit(app.exec_())
