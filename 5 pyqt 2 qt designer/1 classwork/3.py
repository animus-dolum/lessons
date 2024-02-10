import sys
import io
import datetime


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = '''
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>793</width>
    <height>532</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Maximum" vsizetype="Maximum">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="sizePolicy">
    <sizepolicy hsizetype="Maximum" vsizetype="Maximum">
     <horstretch>0</horstretch>
     <verstretch>0</verstretch>
    </sizepolicy>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout_2">
    <item>
     <layout class="QVBoxLayout" name="verticalLayout">
      <item>
       <widget class="QTimeEdit" name="timeEdit"/>
      </item>
      <item>
       <widget class="QCalendarWidget" name="calendarWidget"/>
      </item>
      <item>
       <widget class="QLineEdit" name="lineEdit"/>
      </item>
      <item>
       <widget class="QPushButton" name="addEventBtn">
        <property name="text">
         <string>Добавить событие</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QListWidget" name="eventList"/>
    </item>
    <item>
     <layout class="QVBoxLayout" name="verticalLayout_4"/>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>793</width>
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


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.events = []

        self.addEventBtn.clicked.connect(self.run)

    def run(self):
        date = self.calendarWidget.selectedDate()
        time = self.timeEdit.time()
        dt = datetime.datetime(date.year(), date.month(), date.day(), time.hour(), time.minute())
        self.events.append(str(dt) + ' - ' + str(self.lineEdit.text()))
        self.eventList.clear()
        self.eventList.addItems(list(sorted(self.events)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.setFixedSize(1000, 700)
    ex.setWindowTitle('Минипланировщик')
    ex.show()
    sys.exit(app.exec_())
