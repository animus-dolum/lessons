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


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.degree = 0

        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.orig_image = QImage(fname)
        self.qqqq_image = QImage(fname).copy()
        self.curr_image = QImage(fname).copy()
        self.pixmap = QPixmap(self.curr_image)
        self.image.setPixmap(self.pixmap)

        self.rotateButtons.buttonClicked.connect(self.run_popr_btn)

        self.channelButtons.buttonClicked.connect(self.run_rgball_btn)

        self.lst = {}
        for y in range(self.orig_image.size().width()):
            for x in range(self.orig_image.size().width()):
                point = self.orig_image.pixelColor(x, y).getRgb()
                self.lst[(x, y)] = point
        print(*self.lst.values(), sep='\n')

        self.lst_orig = self.lst.copy()


    def run_rgball_btn(self, btn):
        for y in range(self.curr_image.size().width()):
            for x in range(self.curr_image.size().width()):
                point = self.lst[(x, y)]
                if btn.text() == 'R':
                    self.curr_image.setPixelColor(x, y, QColor(point[0], 0, 0, 255))
                    self.qqqq_image.setPixelColor(x, y, QColor(point[0], 0, 0, 255))
                elif btn.text() == 'G':
                    self.curr_image.setPixelColor(x, y, QColor(0, point[1], 0, 255))
                    self.qqqq_image.setPixelColor(x, y, QColor(0, point[1], 0, 255))
                elif btn.text() == 'B':
                    self.curr_image.setPixelColor(x, y, QColor(0, 0, point[2], 255))
                    self.qqqq_image.setPixelColor(x, y, QColor(0, 0, point[2], 255))
                elif btn.text() == 'ALL':
                    self.curr_image.setPixelColor(x, y, QColor(point[0], point[1], point[2], 255))
                    self.qqqq_image.setPixelColor(x, y, QColor(point[0], point[1], point[2], 255))

        self.pixmap = QPixmap(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def run_popr_btn(self, btn):
        self.degree += 90 * (1 if btn.text() == 'По часовой стрелке' else -1)
        self.curr_image = self.qqqq_image.transformed(QTransform().rotate(self.degree % 360))
        self.orig_image = self.orig_image.transformed(QTransform().rotate(self.degree % 360))
        self.pixmap = QPixmap(self.curr_image)
        self.image.setPixmap(self.pixmap)

        self.lst = {}
        for y in range(self.orig_image.size().width()):
            for x in range(self.orig_image.size().width()):
                point = self.orig_image.pixelColor(x, y).getRgb()
                self.lst[(x, y)] = point
        print(*self.lst.values(), sep='\n')
        self.lst_orig = self.lst.copy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
