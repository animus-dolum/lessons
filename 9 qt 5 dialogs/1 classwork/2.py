import sys
import io


from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage, QTransform, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


template = '''
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>474</width>
    <height>451</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>PIL 2.0</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QPushButton" name="r_btn">
          <property name="text">
           <string>R</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="g_btn">
          <property name="text">
           <string>G</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="b_btn">
          <property name="text">
           <string>B</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="all_btn">
          <property name="text">
           <string>ALL</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="image">
        <property name="minimumSize">
         <size>
          <width>250</width>
          <height>250</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>260</width>
          <height>260</height>
         </size>
        </property>
        <property name="text">
         <string>TextLabel</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QPushButton" name="pr_btn">
        <property name="text">
         <string>Против часовой стрелки</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">rotateButtons</string>
        </attribute>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="po_btn">
        <property name="text">
         <string>По часовой стрелке</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">rotateButtons</string>
        </attribute>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>474</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="rotateButtons"/>
  <buttongroup name="channelButtons"/>
 </buttongroups>
</ui>
'''.strip()


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.degree = 0

        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.orig_image = QImage(fname)
        self.curr_image = QImage(fname).copy()
        self.pixmap = QPixmap(self.curr_image)
        self.image.setPixmap(self.pixmap)

        self.rotateButtons.buttonClicked.connect(self.run_popr_btn)

        self.channelButtons.buttonClicked.connect(self.run_rgball_btn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.exit(app.exec())
