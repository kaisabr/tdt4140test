# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distanceView.ui'
#
# Created: Wed Apr 13 12:24:26 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindowDist(object):
    def setupUi(self, mainWindowDist):
        mainWindowDist.setObjectName("mainWindowDist")
        mainWindowDist.resize(655, 391)
        self.mainWidgetDist = QtGui.QWidget(mainWindowDist)
        self.mainWidgetDist.setObjectName("mainWidgetDist")
        self.gridLayoutWidget = QtGui.QWidget(self.mainWidgetDist)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 631, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.distLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.distLayout.setSpacing(0)
        self.distLayout.setContentsMargins(0, 0, 0, 0)
        self.distLayout.setObjectName("distLayout")
        self.distance_label = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_label.sizePolicy().hasHeightForWidth())
        self.distance_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.distance_label.setFont(font)
        self.distance_label.setStyleSheet("#distance_label{background-color: #0CB90C;}")
        self.distance_label.setFrameShape(QtGui.QFrame.Panel)
        self.distance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_label.setObjectName("distance_label")
        self.distLayout.addWidget(self.distance_label, 1, 0, 1, 1)
        self.speed_label = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_label.sizePolicy().hasHeightForWidth())
        self.speed_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.speed_label.setFont(font)
        self.speed_label.setStyleSheet("#speed_label{background-color: #0CB90C;}")
        self.speed_label.setFrameShape(QtGui.QFrame.Panel)
        self.speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_label.setObjectName("speed_label")
        self.distLayout.addWidget(self.speed_label, 1, 1, 1, 1)
        self.label_disttitle = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_disttitle.sizePolicy().hasHeightForWidth())
        self.label_disttitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.label_disttitle.setFont(font)
        self.label_disttitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disttitle.setObjectName("label_disttitle")
        self.distLayout.addWidget(self.label_disttitle, 0, 0, 1, 1)
        self.label_spdtitle = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_spdtitle.sizePolicy().hasHeightForWidth())
        self.label_spdtitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.label_spdtitle.setFont(font)
        self.label_spdtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spdtitle.setObjectName("label_spdtitle")
        self.distLayout.addWidget(self.label_spdtitle, 0, 1, 1, 1)
        mainWindowDist.setCentralWidget(self.mainWidgetDist)
        self.distMenu = QtGui.QMenuBar(mainWindowDist)
        self.distMenu.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.distMenu.setObjectName("distMenu")
        mainWindowDist.setMenuBar(self.distMenu)

        self.retranslateUi(mainWindowDist)
        QtCore.QMetaObject.connectSlotsByName(mainWindowDist)

    def retranslateUi(self, mainWindowDist):
        mainWindowDist.setWindowTitle(QtGui.QApplication.translate("mainWindowDist", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.distance_label.setText(QtGui.QApplication.translate("mainWindowDist", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.speed_label.setText(QtGui.QApplication.translate("mainWindowDist", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_disttitle.setText(QtGui.QApplication.translate("mainWindowDist", "DISTANCE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_spdtitle.setText(QtGui.QApplication.translate("mainWindowDist", "SPEED", None, QtGui.QApplication.UnicodeUTF8))


