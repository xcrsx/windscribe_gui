# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 450)
        font = QFont()
        font.setFamily(u"Perfect DOS VGA 437")
        font.setBold(True)
        font.setWeight(75);
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/resources/icons/virtual-private-network.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"background-color: #000084;\n"
"")
        self.actionAccountStatus = QAction(MainWindow)
        self.actionAccountStatus.setObjectName(u"actionAccountStatus")
        self.actionShowLoginDialog = QAction(MainWindow)
        self.actionShowLoginDialog.setObjectName(u"actionShowLoginDialog")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.informLabel = QLabel(self.centralwidget)
        self.informLabel.setObjectName(u"informLabel")
        self.informLabel.setGeometry(QRect(10, 5, 380, 87))
        font1 = QFont()
        font1.setFamily(u"Perfect DOS VGA 437")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75);
        self.informLabel.setFont(font1)
        self.informLabel.setStyleSheet(u"color: #defe54;")
        self.informLabel.setFrameShape(QFrame.StyledPanel)
        self.informLabel.setFrameShadow(QFrame.Raised)
        self.informLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.accountStatusButton = QPushButton(self.centralwidget)
        self.accountStatusButton.setObjectName(u"accountStatusButton")
        self.accountStatusButton.setGeometry(QRect(10, 100, 380, 31))
        palette = QPalette()
        brush = QBrush(QColor(187, 187, 187, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.accountStatusButton.setPalette(palette)
        self.accountStatusButton.setFont(font)
        self.accountStatusButton.setStyleSheet(u"QPushButton{\n"
"background-color: #bbbbbb;\n"
"border: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: #666666;\n"
" }\n"
"QPushButton:pressed {\n"
"border-style:solid;\n"
"border-width:3px;\n"
"}")
        self.accountStatusButton.setFlat(True)
        self.mainButton = QPushButton(self.centralwidget)
        self.mainButton.setObjectName(u"mainButton")
        self.mainButton.setGeometry(QRect(10, 140, 381, 50))
        self.mainButton.setFont(font)
        self.mainButton.setAutoFillBackground(False)
        self.mainButton.setStyleSheet(u"QPushButton{\n"
"background-color: #bbbbbb;\n"
"border: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: #666666;\n"
" }\n"
"QPushButton:pressed {\n"
"border-style:solid;\n"
"border-width:3px;\n"
"}")
        self.mainButton.setFlat(True)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(254, 200, 141, 41))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"background-color: #bbbbbb;\n"
"border: 1px\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #00aaaa;\n"
"    color: white;\n"
"	border: 1px;\n"
"    selection-background-color: rgb(88, 88, 88);\n"
"    selection-color: rgb(200, 200, 200);\n"
"}\n"
"QComboBox:hover {\n"
"     background-color: #666666;\n"
" }")
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(10, 200, 91, 31))
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet(u"QPushButton{\n"
"background-color: #bbbbbb;\n"
"border: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: #666666;\n"
" }\n"
"QPushButton:pressed {\n"
"border-style:solid;\n"
"border-width:3px;\n"
"}")
        self.logoutButton.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet(u"color: #defe54;")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.accountStatusButton.clicked.connect(self.actionAccountStatus.trigger)
        self.mainButton.clicked.connect(self.actionShowLoginDialog.trigger)
        self.logoutButton.clicked.connect(self.actionLogout.trigger)
        self.mainButton.clicked.connect(self.actionConnect.trigger)
        self.mainButton.clicked.connect(self.actionDisconnect.trigger)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Windscribe VPN", None))
        self.actionAccountStatus.setText(QCoreApplication.translate("MainWindow", u"checkStat", None))
        self.actionShowLoginDialog.setText(QCoreApplication.translate("MainWindow", u"conDiscon", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.informLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.accountStatusButton.setText(QCoreApplication.translate("MainWindow", u"Check account status", None))
        self.mainButton.setText("")
        self.comboBox.setCurrentText("")
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
    # retranslateUi

