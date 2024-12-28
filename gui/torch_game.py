# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'torch_game.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.time = QLabel(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(10, 20, 31, 37))
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(720, 20, 75, 23))
        self.Torch_one = QPushButton(self.centralwidget)
        self.Torch_one.setObjectName(u"Torch_one")
        self.Torch_one.setGeometry(QRect(390, 80, 51, 41))
        self.Torch_five = QPushButton(self.centralwidget)
        self.Torch_five.setObjectName(u"Torch_five")
        self.Torch_five.setGeometry(QRect(310, 140, 51, 41))
        self.Torch_two = QPushButton(self.centralwidget)
        self.Torch_two.setObjectName(u"Torch_two")
        self.Torch_two.setGeometry(QRect(470, 140, 51, 41))
        self.Torch_three = QPushButton(self.centralwidget)
        self.Torch_three.setObjectName(u"Torch_three")
        self.Torch_three.setGeometry(QRect(420, 200, 51, 41))
        self.Torch_four = QPushButton(self.centralwidget)
        self.Torch_four.setObjectName(u"Torch_four")
        self.Torch_four.setGeometry(QRect(360, 200, 51, 41))
        self.list_record = QListView(self.centralwidget)
        self.list_record.setObjectName(u"list_record")
        self.list_record.setGeometry(QRect(0, 310, 791, 251))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 300, 801, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(720, 50, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 41, 16))
        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(50, 50, 121, 20))
        self.timer_visible = QLabel(self.centralwidget)
        self.timer_visible.setObjectName(u"timer_visible")
        self.timer_visible.setGeometry(QRect(40, 30, 131, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 10))
        self.menubar.setMinimumSize(QSize(700, 10))
        self.menubar.setMaximumSize(QSize(700, 10))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Torch_one.setText("")
        self.Torch_five.setText("")
        self.Torch_two.setText("")
        self.Torch_three.setText("")
        self.Torch_four.setText("")
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.timer_visible.setText("")
    # retranslateUi

