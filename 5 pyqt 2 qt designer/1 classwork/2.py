import sys
import io


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
    <width>634</width>
    <height>534</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>70</y>
      <width>160</width>
      <height>123</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="font">
        <font>
         <pointsize>20</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет №1</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_3">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_1</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_2">
       <property name="text">
        <string>Красный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_1</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_4">
       <property name="text">
        <string>Зелёный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_1</string>
       </attribute>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>70</y>
      <width>160</width>
      <height>123</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="font">
        <font>
         <pointsize>20</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет №2</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_5">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_2</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_6">
       <property name="text">
        <string>Красный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_2</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_7">
       <property name="text">
        <string>Зелёный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_2</string>
       </attribute>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>250</y>
      <width>111</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Сделать флаг</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>220</y>
      <width>341</width>
      <height>251</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>8</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>70</y>
      <width>160</width>
      <height>123</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_3">
     <item>
      <widget class="QLabel" name="label_4">
       <property name="font">
        <font>
         <pointsize>20</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет №3</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_8">
       <property name="text">
        <string>Синий</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_3</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_9">
       <property name="text">
        <string>Красный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_3</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_10">
       <property name="text">
        <string>Зелёный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">color_group_3</string>
       </attribute>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>634</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="color_group_2"/>
  <buttongroup name="color_group_1"/>
  <buttongroup name="color_group_3"/>
 </buttongroups>
</ui>
'''.strip()


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setFixedSize(1000, 1000)

        self.a, self.b, self.c = '', '', ''
        self.lst = ['', '', '']

        self.make_flag.clicked.connect(self.mf)

    def mf(self):
        self.a = ''.join(list(map(lambda x: x.text(), filter(lambda y: y.isChecked(), self.color_group_1.buttons()))))
        self.b = ''.join(list(map(lambda x: x.text(), filter(lambda y: y.isChecked(), self.color_group_2.buttons()))))
        self.c = ''.join(list(map(lambda x: x.text(), filter(lambda y: y.isChecked(), self.color_group_3.buttons()))))
        self.result.setText(f'Цвета: {self.a}, {self.b} и {self.c}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.setWindowTitle('Текстовый флаг')
    ex.show()
    sys.exit(app.exec_())