import sqlite3
import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

template = '''
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>585</width>
    <height>206</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Поиск по фильмам</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QComboBox" name="parameterSelection">
       <property name="minimumSize">
        <size>
         <width>200</width>
         <height>0</height>
        </size>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="queryLine"/>
     </item>
     <item>
      <widget class="QPushButton" name="queryButton">
       <property name="text">
        <string>Поиск</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>ID:</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Название:</string>
       </property>
      </widget>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_5">
       <property name="text">
        <string>Продолжительность:</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Год выпуска:</string>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Жанр:</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="idEdit">
       <property name="enabled">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="titleEdit"/>
     </item>
     <item row="2" column="1">
      <widget class="QLineEdit" name="yearEdit"/>
     </item>
     <item row="3" column="1">
      <widget class="QLineEdit" name="genreEdit"/>
     </item>
     <item row="4" column="1">
      <widget class="QLineEdit" name="durationEdit"/>
     </item>
    </layout>
   </item>
   <item>
    <widget class="QLabel" name="errorLabel">
     <property name="text">
      <string/>
     </property>
    </widget>
   </item>
   <item>
    <spacer name="verticalSpacer">
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="sizeHint" stdset="0">
      <size>
       <width>20</width>
       <height>40</height>
      </size>
     </property>
    </spacer>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''.strip()


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.params = {"Год выпуска": "year", "Название": "title", "Продолжительность": "duration"}
        self.parameterSelection.addItems(list(self.params.keys()))
        self.con = sqlite3.connect("films_db.sqlite")
        self.queryButton.clicked.connect(self.select)

    def select(self):
        try:
            query = self.queryLine.text()
            if not query:
                self.errorLabel.setText("Неправильный запрос")
                return
            t = self.parameterSelection.currentText()
            cur = self.con.cursor()
            result = cur.execute(f"""SELECT * FROM films 
            WHERE {self.params[t]} = ?""", (query,)).fetchone()

            if not result:
                self.errorLabel.setText("Ничего не найдено")
                self.idEdit.setText('')
                self.titleEdit.setText('')
                self.yearEdit.setText('')
                self.genreEdit.setText('')
                self.durationEdit.setText('')
            else:
                self.idEdit.setText(str(result[0]))
                self.titleEdit.setText(str(result[1]))
                self.yearEdit.setText(str(result[2]))
                self.genreEdit.setText(str(result[3]))
                self.durationEdit.setText(str(result[4]))
        except sqlite3.OperationalError:
            self.errorLabel.setText("Неправильный запрос")
            self.idEdit.setText('')
            self.titleEdit.setText('')
            self.yearEdit.setText('')
            self.genreEdit.setText('')
            self.durationEdit.setText('')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
